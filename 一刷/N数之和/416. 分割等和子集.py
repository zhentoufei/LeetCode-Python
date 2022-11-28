class Solution:
    def canPartition(self, nums: list):

        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        max_num = max(nums)
        if total & 1: # 奇数
            return False

        target = total // 2
        if max_num > target:
            return False

        # dp[i][j] 表示从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个），
        # 是否存在一种选取方案使得被选取的正整数的和等于 j

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]