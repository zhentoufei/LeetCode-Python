class Solution:

    def minimumDeleteSum(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)

        # 定义dp[i][j]表示使得 s1[0:i] 和 s2[0:j] 相同的最小ASCII删除和
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]

        for j in range(1, len2 + 1):
            dp[0][j] = ord(s2[j - 1]) + dp[0][j - 1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[-1][-1]
