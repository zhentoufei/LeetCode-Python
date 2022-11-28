class Solution:
    '''
    给你一个 无重复元素 的整数数组, 中的 同一个 数字可以 无限制重复被选取
    '''

    def combinationSum(self, candidates: list, target: int):
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
            track.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, size, track, ans)
            track.pop()

