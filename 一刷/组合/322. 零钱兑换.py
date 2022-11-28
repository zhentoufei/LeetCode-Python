class Solution:

    def combination4(self, nums: list, target: int):
        self.memo = {}
        self.memo[0] = 1
        return self.backtrack(nums, target)

    def backtrack(self, nums: list, target: int):
        if target < 0:
            return 0

        if target in self.memo.keys():
            return self.memo[target]

        ans = 0
        for num in nums:
            ans += self.backtrack(nums, target - num)

        self.memo[target] = ans
        return ans

    def coinChange(self, coins: list, amount: int):
        self.memo = {}
        self.memo[0] = 1
        self.amount = amount + 1
        self.ans = amount + 1
        return self.backtrack_coin(coins, amount)

    def backtrack_coin(self, coins: list, target: int):
        if target < 0:
            return self.amount + 1

        if target in self.memo.keys():
            self.ans = min(self.ans, self.memo[target])
            return self.memo[target]
        tmp = 0
        for coin in coins:
            # print(coin)
            tmp += self.backtrack_coin(coins, target - coin)

        self.memo[target] = min(self.ans, tmp)
        return self.memo[target]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    cls = Solution()
    print(cls.coinChange(coins, amount))
