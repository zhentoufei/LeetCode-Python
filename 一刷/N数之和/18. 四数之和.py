class Solution:

    def fourSum(self, nums:list, target:int):

        nums = sorted(nums)
        length = len(nums)
        if nums is None or length <= 3:
            return []

        res = []

        for i in range(length - 3):

            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue

            for j in range(i + 1, length - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue

                left = j + 1
                right = length - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if target == total:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        left += 1

                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
