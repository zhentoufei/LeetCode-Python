class Solution:

    def nextPermutation(self, nums: list):

        size = len(nums)
        i = size - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        j = size - 1
        if i >= 0:
            while j > i and nums[i] >= nums[j]:
                j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = size - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [2, 3, 1]
    cls = Solution()
    print(cls.nextPermutation(nums))
    print(nums)
