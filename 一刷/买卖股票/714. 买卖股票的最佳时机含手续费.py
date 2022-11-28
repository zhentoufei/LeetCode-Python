class Solution:

    def maxProfit(self, prices:list, fee: int):
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]

        for i in range(length):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -1 * prices[i] - fee
            else:
                dp[i][0] = max(dp[i-1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return dp[length - 1][0]

