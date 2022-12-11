class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: TreeNode):
        if not root:
            return 0

        level = 0
        node = root
        while node.left is not None:
            level += 1
            node = node.left

        low = 1 << level
        high = (1 << (level + 1)) - 1

        while low < high:
            mid = (high - low + 1) // 2 + low
            if self.exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low

    # 完整二叉树数据是否存在的问题
    def exists(self, root: TreeNode, level: int, k: int):
        bits = 1 << (level - 1)
        node = root
        while node is not None and bits > 0:
            tmp = bits & k
            if tmp == 0:
                node = node.left
            else:
                node = node.right

            bits >>= 1

        return node != None


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    cls = Solution()
    print(cls.countNodes(t1))
