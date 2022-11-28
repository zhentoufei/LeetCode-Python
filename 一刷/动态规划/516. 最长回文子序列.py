class Solution:
    '''
    用 dp[i][j] 表示字符串 s 的下标范围[i,j] 内的最长回文子序列的长度
    '''
    def longestPalindromeSubseq(self, s: str):

        length = len(s)
        dp = [[0] * length for _ in range(length)]

        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][length - 1]
