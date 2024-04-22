class Solution:
    def lengthOfLongestSubsequence(self, nums: list, target: int) -> int:
        f = [0] + [float('-inf')] * target
        s = 0
        for x in nums:
            s = min(s + x, target)
            for j in range(s, x - 1, -1):
                f[j] = max(f[j], f[j - x] + 1)
        return f[-1] if f[-1] > 0 else -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(Solution().lengthOfLongestSubsequence(nums, target))
