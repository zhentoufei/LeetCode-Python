class Solution:

    def longestPalindrome(self, s: str):
        length = len(s)
        res = ''
        for i in range(length):
            s1 = self.isPalind(s, i, i, length)
            s2 = self.isPalind(s, i, i + 1, length)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def isPalind(self, s: str, left: int, right: int, length: int):
        while left >= 0 and right <= length - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]
