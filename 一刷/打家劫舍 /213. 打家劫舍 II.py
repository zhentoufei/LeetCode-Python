class Solution:

    def rob(self, nums: list):
        size = len(nums)
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])
        else:
            return max(self.robHelper(nums[0:-1]), self.robHelper(nums[1:]))

    def robHelper(self, nums: list):
        size = len(nums)
        if size == 1:
            return nums[0]

        if size == 2:
            return max(nums[0], nums[1])

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    cls = Solution()
    print(cls.rob(nums))
