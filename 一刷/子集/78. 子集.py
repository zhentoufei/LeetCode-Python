class Solution:

    def subsets(self, nums: list):
        size = len(nums)
        ans = []
        self.backtrack(nums, [], ans, 0, size)
        return ans

    def backtrack(self, nums: list, track: list, ans: list, start: int, size: int):
        ans.append(track[:])
        for i in range(start, size):
            track.append(nums[i])
            self.backtrack(nums, track, ans, i + 1, size)
            track.pop()
