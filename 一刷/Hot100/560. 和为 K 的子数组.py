class Solution:

    def subarraySum(self, nums: list, k: int):
        ans = 0
        pre = 0
        memo = {0: 1}
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in memo.keys():
                ans += memo[pre - k]

            if pre not in memo.keys():
                memo[pre] = 0
            memo[pre] += 1
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    so = Solution()
    print(so.subarraySum(nums, k))
