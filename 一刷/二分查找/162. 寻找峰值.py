class Solution:

    def findPeakElement(self, nums: list):
        size = len(nums)
        left = 0
        right = size - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if self.get(mid - 1, nums) < self.get(mid, nums) > self.get(mid + 1, nums):
                return mid

            if self.get(mid, nums) < self.get(mid + 1, nums):
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get(self, index: int, nums: list):
        if index == -1 or index == len(nums):
            return float('-inf')
        return nums[index]
