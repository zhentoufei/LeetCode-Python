class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:

        # https://leetcode.cn/problems/target-sum/solution/mu-biao-he-by-leetcode-solution-o0cp/
        # pos - neg = target = sum - 2 * neg = target
        diff = sum(nums) - target

        if diff < 0 or diff % 2 != 0:
            return 0

        neg = int(diff / 2)
        sizeOfNums = len(nums)
        # 定义二维数组 dp，其中 dp[i][j] 表示在数组 nums 的前 i 个数中选取元素，使得这些元素之和等于 j 的方案数
        dp = [[0] * (neg + 1) for _ in range(sizeOfNums + 1)]

        dp[0][0] = 1
        for numIndex in range(1, sizeOfNums + 1, 1):
            currentNum = nums[numIndex - 1]
            for targetIndex in range(0, neg + 1, 1):
                if targetIndex >= currentNum:
                    dp[numIndex][targetIndex] = dp[numIndex - 1][targetIndex] \
                                                + dp[numIndex - 1][targetIndex - currentNum]
                else:
                    dp[numIndex][targetIndex] = dp[numIndex - 1][targetIndex]

        return dp[sizeOfNums][neg]
