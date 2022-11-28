class Solution:

    def permute(self, nums: list):
        size = len(nums)
        ans = []
        used = [False] * size
        self.backtrack(nums, used, [], ans, size)
        return ans

    def backtrack(self, nums: list, used: list, track: list, ans: list, size: int):

        if len(track) == size:
            ans.append(track[:])

        for i in range(size):
            if not used[i]:
                track.append(nums[i])
                used[i] = True
                self.backtrack(nums, used, track, ans, size)
                used[i] = False
                track.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    cls = Solution()
    print(cls.permute(nums))
