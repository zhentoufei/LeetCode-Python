class Solution:

    def twoSum(self, nums: list, target: int):

        memo = {}
        for i, num in enumerate(nums):

            tmp = target - num
            if tmp in memo.keys():
                return [memo[tmp], i]
            else:
                memo[num] = i

        return [-1, -1]


