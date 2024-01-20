class Solution:

    def threeSum(self, nums):

        nums = sorted(nums)
        ans = []
        size = len(nums)
        for i in range(size):
            if nums[i] > 0:
                return ans

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = size - 1
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if tmp_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return ans


if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums))