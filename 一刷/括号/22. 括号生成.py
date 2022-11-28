class Solution:

    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int):
        self.backtrack([], 0, 0, n)
        return self.ans

    def backtrack(self, s: list, left:int, right:int, n: int):

        if len(s) == 2 * n:
            self.ans.append(''.join(s))
        else:
            if left < n:
                s.append('(')
                self.backtrack(s, left + 1, right, n)
                s.pop()

            if right < left:
                s.append(')')
                self.backtrack(s, left, right + 1, n)
                s.pop()


