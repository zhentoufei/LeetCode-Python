class Solution:

    def coinChange(self, coins: list, amount: int):
        ans = [amount + 1] * (amount + 1)
        ans[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if 1 + ans[i - coin] < ans[i]:
                    ans[i] = 1 + ans[i - coin]
        return ans[-1] if ans[-1] != amount + 1 else -1

    def coinChangev1(self, coins: list, amount: int):
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)
