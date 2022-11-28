class Solution:

    def searchRange(self, nums: list, target: int):

        if len(nums) == 0:
            return [-1, -1]
        first_pos = self.findFirstPos(nums, target)
        if first_pos == -1:
            return [-1, -1]
        second_pos = self.findSecondPos(nums, target)
        return [first_pos, second_pos]

    def findFirstPos(self, nums, target):

        left = 0
        right = len(nums) - 1
        while left < right:

            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1

    def findSecondPos(self, nums: list, target: int):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left + 1)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1
