class Solution:

    def combination3(self, k: int, n: int):
        ans = []
        self.backtrack(k, n, 1, [], ans)
        return ans

    def backtrack(self, k: int, n: int, start: int, track: list, ans: list):
        if k < 0 or n < 0:
            return

        if k == 0 and n == 0:
            ans.append(track[:])
            return

        for i in range(start, 10):
            track.append(i)
            self.backtrack(k - 1, n - i, i + 1, track, ans)
            track.pop()
