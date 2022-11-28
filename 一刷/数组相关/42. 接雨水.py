class Solution:

    def trap(self, height:list):

        size = len(height)
        max_left = [0] * size

        for i in range(1, size, 1):
            max_left[i] = max(height[i - 1], max_left[i - 1])

        max_right = [0] * size
        for i in range(size - 2, 0, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        ans = 0
        for i in range(1, size - 1, 1):
            tmp = min(max_left[i], max_right[i])
            if tmp > height[i]:
                ans = ans + tmp - height[i]

        return ans
