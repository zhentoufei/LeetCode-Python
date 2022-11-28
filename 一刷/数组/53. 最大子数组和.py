class Solution:

    def maxSubArray(self, nums:list):

        size = len(nums)
        pre = 0
        ans = nums[0]
        for i in range(size):
            pre = max(nums[i], pre + nums[i])
            ans = max(ans, pre)

        return ans