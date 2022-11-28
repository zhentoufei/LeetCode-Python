class Solution:

    def minDistance(self, word1: str, word2: str):

        size1 = len(word1)
        size2 = len(word2)

        if size2 * size1 == 0:
            return size1 + size2

        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]

        for i in range(size1 + 1):
            dp[i][0] = i

        for j in range(size2 + 1):
            dp[0][j] = j

        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                left = dp[i - 1][j] + 1
                up = dp[i][j - 1] + 1
                left_up = dp[i - 1][j - 1]

                if word1[i - 1] != word2[j - 1]:
                    left_up += 1

                dp[i][j] = min(left, up, left_up)
        return dp[-1][-1]
