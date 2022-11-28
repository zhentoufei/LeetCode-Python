class Solution:

    def subsetsWithDup(self, nums: list):
        nums = sorted(nums)
        ans = []
        self.backtrack(nums, [], ans, 0, len(nums))
        return ans

    def backtrack(self, nums: list, track: list, ans: list, start: int, size: int):
        ans.append(track[:])

        for i in range(start, size):
            if i > start and nums[i] == nums[i - 1]:
                continue

            track.append(nums[i])
            self.backtrack(nums, track, ans, i + 1, size)
            track.pop()
