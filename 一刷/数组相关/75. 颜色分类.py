class Solution:

    def sortColors(self, nums: list):

        n = len(nums)
        p0 = 0
        p1 = 0

        for i in range(n):

            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]

                p0 += 1
                p1 += 1

