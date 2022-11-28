class Solution:

    def search(self, nums: list, target: int):

        if not nums:
            return False

        if len(nums) == 1:
            return nums[0] == target

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    cls = Solution()
    nums = [5, 1, 3]
    print(cls.search(nums, 3))
