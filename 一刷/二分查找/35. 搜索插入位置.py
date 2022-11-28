class Solution:

    def searchInsert(self, nums: list, target: int):
        size = len(nums)
        left = 0
        right = size - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

        return left

    def binarySearch(self, nums:list, target:int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

    def leftBound(self, nums: list, target: int):
        left = 0

        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                right = mid - 1
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    def rigthBound(self, nums: list, target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        if left - 1 < 0:
            return -1
        return left - 1 if nums[left - 1] == target else -1


if __name__ == '__main__':
    cls = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(cls.searchInsert(nums, target))
