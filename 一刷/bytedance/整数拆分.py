class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        创建数组 dp，其中 dp[i]表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。
        特别地，0 不是正整数，1 是最小的正整数，0 和 1 都不能拆分，因此 dp[0]=dp[1]=0

        case1: 将 i 拆分成 j 和 i−j的和，且 i−j不再拆分成多个正整数，此时的乘积是 j×(i−j)
        case2: 将 i 拆分成 j 和 i−j的和，且 i−j继续拆分成多个正整数，此时的乘积是 j×dp[i−j]
        '''
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]
