class Solution:

    def trap(self, height):

        if len(height) == 1:
            return 0

        size = len(height)
        left = [0] * size
        right = [0] * size
        for i in range(1, size, 1):
            left[i] = max(height[i - 1], left[i - 1])

        for i in range(size - 2, 0, -1):
            right[i] = max(height[i + 1], right[i + 1])

        ans = 0
        for i in range(1, size - 1, 1):
            current = min(left[i], right[i])
            if current > height[i]:
                ans = ans + current - height[i]
        return ans


if __name__ == '__main__':
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(h))
