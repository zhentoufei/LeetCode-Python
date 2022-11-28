class Solution:

    def longestValidParentheses(self, s: str):

        length = len(s)
        ans = 0

        if length == 0:
            return ans

        dp = [0] * length

        for i in range(length):
            if i > 0 and s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2 if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2


        return max(dp)

if __name__ == '__main__':
    s = "(()())"
    cls = Solution()
    print(cls.longestValidParentheses(s))