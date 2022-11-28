class Solution:

    def maxProfit(self, prices: list):

        size = len(prices)
        # dp[0][0] 第0天，手上不持有股票
        # dp[0][1] 第0天，手上持有股票
        dp = [[0] * 2 for _ in range(size)]

        for i in range(size):

            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[size-1][0]
