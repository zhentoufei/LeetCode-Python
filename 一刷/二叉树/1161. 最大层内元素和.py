class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxLevelSum(self, root: TreeNode):

        max_level = 0
        level = 0
        max_sum = float('-inf')

        memo = []
        memo.append(root)
        while memo:
            size = len(memo)
            tmp_sum = 0
            level += 1
            for _ in range(size):
                node = memo.pop(0)
                tmp_sum += node.val
                if node.left:
                    memo.append(node.left)

                if node.right:
                    memo.append(node.right)

            if tmp_sum > max_sum:
                max_sum = tmp_sum
                max_level = level
        return max_level

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(7)
    t3 = TreeNode(0)
    t4 = TreeNode(7)
    t5 = TreeNode(-8)

