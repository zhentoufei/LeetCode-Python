class Solution:

    def checkSubarraySum(self, nums: list, k: int):
        size = len(nums)
        if size < 2:
            return False

        memo = {}
        memo[0] = -1
        remainder = 0
        for i in range(size):
            remainder = (remainder + nums[i]) % k
            if remainder in memo.keys():
                pre_index = memo.get(remainder)
                if i - pre_index >= 2:
                    return True
            else:
                memo[remainder] = i

        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    cls = Solution()
    cls.checkSubarraySum(nums, k)