class Solution:
    '''
    和为奇数的子数列的数目
    '''

    def numOfSubarrays1(self, arr: list) -> int:
        size = len(arr)
        dp_odd = [0] * size  # 和为奇数的dp，dp_odd[i]表示，以arr[i]为结尾，且子数组的和是奇数的子序列的个数
        dp_even = [0] * size  # 和为偶数的dp

        ans = 0
        if arr[0] % 2 != 0:
            dp_odd[0] = 1
        else:
            dp_even[0] = 1
        ans += dp_odd[0]

        for i in range(1, size):
            # 奇数+偶数=奇数;奇数+奇数=偶数
            # 偶数+奇数=奇数;偶数+偶数=偶数
            if arr[i] % 2 != 0:
                dp_odd[i] = dp_even[i - 1] + 1
                dp_even[i] = dp_odd[i - 1] + 0
            else:
                dp_odd[i] = dp_odd[i - 1] + 0
                dp_even[i] = dp_even[i - 1] + 1
            ans += dp_odd[i]
        return int(ans % 1000000007)

    def numOfSubarrays2(self, arr: list) -> int:
        # 空间复杂度优化过的
        size = len(arr)
        dp_odd = 0  # 和为奇数的dp
        dp_even = 0  # 和为偶数的dp

        ans = 0
        if arr[0] % 2 != 0:
            dp_odd = 1
        else:
            dp_even = 1

        dp_odd_old = dp_odd
        dp_even_old = dp_even
        ans += dp_odd

        for i in range(1, size):
            # 奇数+偶数=奇数;奇数+奇数=偶数
            # 偶数+奇数=奇数;偶数+偶数=偶数
            if arr[i] % 2 != 0:
                dp_odd = dp_even_old + 1
                dp_even = dp_odd_old + 0
            else:
                dp_odd = dp_odd_old + 0
                dp_even = dp_even_old + 1

            dp_odd_old = dp_odd
            dp_even_old = dp_even
            ans += dp_odd
        return int(ans % (1000000007))

    '''
    求子序列的最大和
    '''

    def max_sum_of_sub_arr(self, nums: list):
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    '''
    求子序列的最大和，且这个和必须是奇数
    '''

    def max_odd(self, nums: list):
        size = len(nums)
        dp_odd = [0] * size
        dp_eve = [0] * size

        if nums[0] % 2 != 0:  # odd
            dp_odd[0] = nums[0]
        else:
            dp_eve[0] = nums[0]

        for i in range(1, size):
            if nums[i] % 2 != 0:
                dp_odd[i] = max(dp_eve[i - 1] + nums[i], dp_odd[i - 1])
                dp_eve[i] = max(dp_odd[i - 1] + nums[i], dp_eve[i - 1])
            else:
                dp_odd[i] = max(dp_odd[i - 1] + nums[i], dp_odd[i - 1])
                dp_eve[i] = max(dp_eve[i - 1] + nums[i], dp_eve[i - 1])
        return max(dp_odd)
