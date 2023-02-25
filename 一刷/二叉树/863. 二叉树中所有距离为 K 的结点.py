class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.node_2_parent = {}
        self.ans = []

    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        self.find_parent(root)
        print(self.node_2_parent.items())
        self.find_kth(target, None, 0, k)
        return self.ans

    def find_parent(self, node: TreeNode):
        if node.left:
            self.node_2_parent[node.left.val] = node
            self.find_parent(node.left)
        if node.right:
            self.node_2_parent[node.right.val] = node
            self.find_parent(node.right)

    def find_kth(self, node: TreeNode, source: TreeNode, depth: int, k: int):
        if not node:
            return
        if depth == k:
            self.ans.append(node.val)
            return

        if node.left != source:
            self.find_kth(node.left, node, depth + 1, k)

        if node.right != source:
            self.find_kth(node.right, node, depth + 1, k)

        if node.val in self.node_2_parent.keys() and self.node_2_parent[node.val] != source:
            self.find_kth(self.node_2_parent[node.val], node, depth + 1, k)


def list_2_tree(nums: list):
    head = TreeNode(nums.pop(0))
    root = head
    node_queue = [head]
    while nums:
        if not node_queue:
            val = nums.pop(0)
            node = TreeNode(val)
            node_queue.append(node)
        else:
            current_node = node_queue.pop(0)
            current_node.left = TreeNode(nums.pop(0))
            if nums:
                current_node.right = TreeNode(nums.pop(0))
    return root


def array_to_bitree_2(array):
    if len(array) == 0:
        return TreeNode(-1)
    root = TreeNode(array[0])
    node_list = [root]
    for i in range(1, len(array)):
        val = array[i]
        node = TreeNode(val)
        node_list.append(node)
        if i % 2 == 1:
            node_list[int((i - 1) / 2)].left = node
        if i % 2 == 0:
            node_list[int((i - 2) / 2)].right = node

    return root


if __name__ == '__main__':
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    target = TreeNode(5)
    k = 2
    cls = Solution()
    root = array_to_bitree_2(nums)
    print(cls.distanceK(root, target, k))
