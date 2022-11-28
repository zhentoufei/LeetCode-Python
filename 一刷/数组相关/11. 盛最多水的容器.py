class Solution:

    def maxArea(self, height: list):
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:

            if height[left] > height[right]:
                ans = max(ans, height[right] * (right - left))
                right -= 1
            else:
                ans = max(ans, height[left] * (right - left))
                left += 1

        return ans