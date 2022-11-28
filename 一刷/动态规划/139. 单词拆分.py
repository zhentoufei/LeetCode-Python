class Solution:

    def wordBreak(self, s: str, wordDict: list):

        word_set = set(wordDict)
        size = len(s)
        # 定义 dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0..i−1] 是否能被空格拆分成若干个字典中出现的单词
        res = [False] * (size + 1)

        res[0] = True

        for i in range(1, size + 1):
            for j in range(0, i):
                if res[j] == True and s[j:i] in word_set:
                    res[i] = True
                    break
        return res[-1]
