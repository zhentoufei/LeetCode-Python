class Solution:

    def combination4(self, nums:list, target:int):
        self.memo = {}
        self.memo[0] = 1
        return self.backtrack(nums, target)

    def backtrack(self, nums:list, target:int):
        if target < 0:
            return 0

        if target in self.memo.keys():
            return self.memo[target]

        ans = 0
        for num in nums:
            ans += self.backtrack(nums, target - num)

        self.memo[target] = ans
        return ans