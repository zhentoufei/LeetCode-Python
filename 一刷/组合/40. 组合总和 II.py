class Solution:

    def combinationSum2(self, candidates: list, target: int):
        candidates = sorted(candidates)
        size = len(candidates)
        ans = []
        self.backtrack(candidates, target, 0, size, [], ans)
        return ans

    def backtrack(self, candidates: list, target: int, start: int, size: int, track: list, ans: list):

        if target < 0:
            return

        if target == 0:
            ans.append(track[:])
            return

        for i in range(start, size):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            track.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, size, track, ans)
            track.pop()
