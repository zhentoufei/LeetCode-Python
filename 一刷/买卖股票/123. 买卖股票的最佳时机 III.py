class Solution:

    def maxProfit(self, prices: list):

        size = len(prices)
        dp1 = [[0] * 2 for _ in range(size)]
        dp2 = [[0] * 2 for _ in range(size)]

        for i in range(size):
            if i == 0:
                dp1[i][0] = 0
                dp1[i][1] = -prices[i]
                dp2[i][0] = 0
                dp2[i][1] = -prices[i]
            else:
                dp1[i][1] = max(dp1[i - 1][1], - prices[i])
                dp1[i][0] = max(dp1[i - 1][0], dp1[i - 1][1] + prices[i])
                dp2[i][1] = max(dp2[i - 1][1], dp1[i - 1][0] - prices[i])
                dp2[i][0] = max(dp2[i - 1][0], dp2[i - 1][1] + prices[i])

        return dp2[-1][0]
