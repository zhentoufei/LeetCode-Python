class Solution:


    def threeSum(self, nums:list):

        nums = sorted(nums)
        length = len(nums)
        res = []
        for i in range(length):
            if nums[i] > 0:
                return res

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1
            while left < right:

                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1


        return res