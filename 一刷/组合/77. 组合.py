class Solution:

    def combine(self, n: int, k: int):
        ans = []
        self.backtrack(n, k, 0, [], ans)
        return ans

    def backtrack(self, n: int, k: int, start: int, track: list, ans: list):
        if k == 0:
            return ans.append(track[:])

        for i in range(start, n):
            track.append(i + 1)
            self.backtrack(n, k - 1, i + 1, track, ans)
            track.pop()
