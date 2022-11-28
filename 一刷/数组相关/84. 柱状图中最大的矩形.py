class Solution:

    def largestRectangleArea(self, heights: list):

        size = len(heights)
        left = [0] * size
        right = [0] * size
        memo = []

        for i in range(size):

            while memo and heights[memo[-1]] >= heights[i]:
                memo.pop()
            left[i] = memo[-1] if memo else -1
            memo.append(i)

        memo = []
        for i in range(size - 1, -1, -1):
            while memo and heights[memo[-1]] >= heights[i]:
                memo.pop()

            right[i] = memo[-1] if memo else size  # 注意这里的兜底值是size，保证是最右边
            memo.append(i)

        ans = max([(right[i] - left[i] - 1) * heights[i] for i in range(size)])
        return ans
