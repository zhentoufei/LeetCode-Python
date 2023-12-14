import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestZigZag(self, root: TreeNode):
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)

        memo = collections.deque([(root, None)])
        while len(memo) > 0:
            node, parent = memo.popleft()
            if parent:
                if parent.left == node:
                    left[node] = right[parent] + 1
                else:
                    right[node] = left[parent] + 1

            if node.left:
                memo.append((node.left, node))

            if node.right:
                memo.append((node.right, node))

        ans = 0
        for _, val in left.items():
            ans = max(ans, val)

        for _, val in right.items():
            ans = max(ans, val)

        return ans
