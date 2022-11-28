class Solution:

    def removeDuplicates(self, nums:list):

        length = len(nums)
        if length == 1:
            return 1

        slow = 0
        for i in range(1, length):
            if nums[i] == nums[slow]:
                continue

            nums[slow + 1] = nums[i]
            slow += 1
        return slow + 1