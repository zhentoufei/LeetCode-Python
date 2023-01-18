class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTrees(self, n: int):
        return self.traveral(1, n)

    def traveral(self, start, end):
        if start > end:
            return [None, ]

        all_trees = []
        for i in range(start, end + 1):  # 闭区间
            left_trees = self.traveral(start, i - 1)
            right_tress = self.traveral(i + 1, end)

            for l in left_trees:
                for r in right_tress:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r

                    all_trees.append(current_tree)
        return all_trees
