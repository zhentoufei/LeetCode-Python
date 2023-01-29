class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int):
        stack = []
        tmp_node = root
        while tmp_node is not None or len(stack) != 0:
            if tmp_node is not None:
                stack.append(tmp_node)
                tmp_node = tmp_node.left
            else:
                tmp_node = stack.pop()
                k = k - 1
                if k == 0:
                    return tmp_node.val
                tmp_node = tmp_node.right

