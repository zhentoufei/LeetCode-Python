class Solution:

    def lengthOfLongestSubstring(self, s: str):

        memo = {}
        left = 0
        right = 0
        length = len(s)
        ans = 0

        while left <= right and right <= length - 1:
            move_in = s[right]
            right += 1

            if move_in not in memo.keys():
                memo[move_in] = 0
            memo[move_in] += 1

            while memo[move_in] > 1:
                move_out = s[left]
                memo[move_out] -= 1
                left += 1
            ans = max(ans, right - left)
        return ans
