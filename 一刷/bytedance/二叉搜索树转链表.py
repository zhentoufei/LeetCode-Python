class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treenode_2_listnode(self, root: TreeNode):
        self.list_node = []
        self.pre_order_rec(root)
        size = len(self.list_node)
        print(self.list_node)
        dummy = self.list_node[size - 1]
        for i in range(size - 1 - 1, -1, -1):
            previous, current = dummy, self.list_node[i]
            previous.right = None
            previous.left = current
        return dummy

    def pre_order_rec(self, root: TreeNode):
        if root:
            self.list_node.append(root)
            self.pre_order_rec(root.left)
            self.pre_order_rec(root.right)

    def mergeSort(self, nums: list):
        """
        归并排序 O(nlogn) 空间复杂度O(n) 稳定排序

        申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        重复步骤 3 直到某一指针达到序列尾；
        将另一序列剩下的所有元素直接复制到合并序列尾。

        """
        size = len(nums)
        if size < 2:
            return nums

        mid = size // 2
        return self.merge(self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:]))
    def merge(self, left: list, right: list):
        result = []
        while left and right:
            if left[0] >= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while left:
            result.append(left.pop(0))

        while right:
            result.append(right.pop(0))
        return result


if __name__ == '__main__':

    a3 = TreeNode(3)
    a1 = TreeNode(1)
    a2 = TreeNode(2, left=a1, right=a3)
    so = Solution()
    ans = so.treenode_2_listnode(a2)
    print(f'root val: {ans.val}, roo.left val:{ans.left.val}')
