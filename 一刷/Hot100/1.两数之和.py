class Solution:

    def twoSum(self, nums, target):
        memo = {}
        for index, value in enumerate(nums):
            tmp = target - value
            if tmp in memo.keys():
                return [memo[tmp], index]
            else:
                memo[value] = index
        return [-1, -1]