class Solution:

    def missingNumber(self, nums: list):

        agg = 0
        for i in nums:
            agg += i

        size = len(nums)

        return (1 + size) * size / 2 - agg

    def missingNumber1(self, nums: list):

        xor = 0
        for i in nums:
            xor ^= i

        for i in range(len(nums)):
            xor ^= i

        return xor
