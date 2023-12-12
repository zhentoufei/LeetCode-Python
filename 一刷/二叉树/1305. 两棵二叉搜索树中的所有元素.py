class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode):

        def inorder(node: TreeNode, seq: list):
            if node:
                inorder(node.left, seq)
                seq.append(node.val)
                inorder(node.right, seq)

        seq_1 = []
        seq_2 = []
        inorder(root1, seq_1)
        inorder(root2, seq_2)

        index_1, index_2 = 0, 0
        size_1, size_2 = len(seq_1), len(seq_2)

        ans = []
        while True:

            if index_1 == size_1:
                ans.extend(seq_2[index_2:])
                break

            if index_2 == size_2:
                ans.extend(seq_1[index_1:])
                break

            if seq_1[index_1] < seq_2[index_2]:
                ans.append(seq_1[index_1])
                index_1 += 1
            else:
                ans.append(seq_2[index_2])
                index_2 += 1
        return ans
