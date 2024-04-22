class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        self.ans = []
        #  dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列的长度。
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # 如果要打印出来子序列，那么就使用flag矩阵
        self.flag = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    self.flag[i][j] = 0
                else:
                    if dp[i - 1][j] >= dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                        self.flag[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                        self.flag[i][j] = -1

        self.printLCS(text1, len1, len2)
        print(f'the ans of seq is {self.ans}')
        return dp[-1][-1]

    def printLCS(self, text1: str, i: int, j: int):
        if i == 0 or j == 0:
            return

        if self.flag[i][j] == 0:
            self.printLCS(text1, i - 1, j - 1)
            self.ans.append(text1[i - 1])
        elif self.flag[i][j] == 1:
            self.printLCS(text1, i - 1, j)
        else:
            self.printLCS(text1, i, j - 1)


if __name__ == '__main__':
    text1 = "abc"
    text2 = "def"
    so = Solution()
    print(so.longestCommonSubsequence(text1, text2))
