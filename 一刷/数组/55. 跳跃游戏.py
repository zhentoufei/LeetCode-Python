class Solution:

    def canJump(self, nums:list):
        size = len(nums)
        right_most = 0
        for i in range(size):
            # if i <= right_most:
            right_most = max(right_most, nums[i] + i)
            if right_most >= size - 1:
                return True
        return False