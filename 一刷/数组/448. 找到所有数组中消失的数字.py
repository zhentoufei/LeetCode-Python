class Solution:

    def findDisappearedNumbers(self, nums:list):
        size = len(nums)
        for num in nums:
            x = (num - 1) % size
            nums[x] += size

        return [i + 1 for i, num in enumerate(nums) if num <= size]