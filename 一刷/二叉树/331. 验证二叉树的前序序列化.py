class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    '''
    https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/solution/pai-an-jiao-jue-de-liang-chong-jie-fa-zh-66nt/
    '''
    def isValidSerialization(self, preorder: str):
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')

        return len(stack) == 1 and stack.pop() == '#'


class Solution2:

    def isValidSerialization(self, preorder: str):
        diff = 1
        for node in preorder.split(","):
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2

        return diff == 0


