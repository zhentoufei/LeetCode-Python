class Solution:

    def majorityElement(self, nums: list):
        nums.sort()
        return nums[len(nums) // 2]
