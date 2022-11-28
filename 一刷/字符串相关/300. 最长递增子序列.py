# 定义 dp[i] 为考虑前 ii 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意 nums[i] 必须被选取。

class Solution:

    def lengthOfLIS(self, nums: list):

        if nums is None or len(nums) == 0:
            return 0

        length = len(nums)
        dp = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
