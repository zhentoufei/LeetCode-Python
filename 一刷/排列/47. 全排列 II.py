class Solution:

    def permuteUnique(self, nums: list):
        nums = sorted(nums)
        size = len(nums)
        ans = []
        used = [False] * size


    def backtrack(self, nums:list, used:list, track:list, ans:list, size:int):

        if len(track) == size:
            ans.append(track[:])
            return

        for i in range(size):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                track.append(nums[i])
                used[i] = True
                self.backtrack(nums, used, track, ans, size)
                used[i] = False
                track.pop()