class Solution:

    def twoSum(self, nums:list, target:int):
        left = 0
        right = len(nums) - 1
        while left < right:
            agg = nums[left] + nums[right]
            if agg == target:
                return [left, right]
            elif agg < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]