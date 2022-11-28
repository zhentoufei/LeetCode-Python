class Solution:

    def singleNumber(self, nums: list):
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i] # 异或

        return res
