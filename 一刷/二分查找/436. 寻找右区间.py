class Solution:

    def findRightInterval(self, intervals: list):
        start_map = {interval[0]: i for i, interval in enumerate(intervals)}
        starts = [interval[0] for interval in intervals]
        ans = []
        starts.sort()
        for interval in intervals:
            pos = self.higher_find(starts, interval[1])
            ans.append(start_map[starts[pos]] if pos != -1 else -1)
        return ans

    def higher_find(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left >= len(nums) or nums[left] < target:
            return -1
        return left
