class Solution:

    def removeElement(self, nums:list, val: int):
        length = len(nums)
        slow = 0
        for i in range(length):

            if nums[i] == val:
                continue

            nums[slow] = nums[i]
            slow += 1

        return slow