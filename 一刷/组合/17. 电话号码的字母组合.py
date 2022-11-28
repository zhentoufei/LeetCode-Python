class Solution:

    def __init__(self):
        self.comb = []
        self.combs = []
        self.word_info = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

    def letterCombinations(self, digits: str):

        if len(digits) == 0:
            return self.combs
        self.dfs(0, digits)
        return self.combs

    def dfs(self, index: int, digits: str):
        if index == len(digits):
            self.combs.append(''.join(self.comb))
        else:
            num = digits[index]
            for ele in self.word_info[num]:
                self.comb.append(ele)
                self.dfs(index + 1, digits)
                self.comb.pop()

