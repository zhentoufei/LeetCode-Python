class Solution:

    def maxProfit(self, prices:list):
        size = len(prices)
        dp = [[0] * 2 for _ in range(size)]

        for i in range(size):

            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            elif i == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]