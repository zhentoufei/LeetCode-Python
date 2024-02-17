# https://www.bilibili.com/video/BV1d54y1q7k7/?spm_id_from=333.337.search-card.all.click&vd_source=6eb66f36703a554cc83a9f4cb7f5560a

class Solution:
    def find_target_1st(self, nums: list, target: int):

        left = -1
        right = len(nums)

        while left + 1 != right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right

    def find_target_last(self, nums: list, target: int):

        left = -1
        right = len(nums)

        while left + 1 != right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        return left

    def find_1st(self, nums, target):
        left = -1
        right = len(nums)
        while left + 1 != right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if right < len(nums) and nums[right] == target:
            return right
        return -1


if __name__ == '__main__':
    cls = Solution()
    nums = [2, 2]
    target = 3
    print(cls.find_1st(nums, target))
