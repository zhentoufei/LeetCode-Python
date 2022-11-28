class Solution:

    def maxEnveloopes(self, envelopes: list):

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = []
        for ele in envelopes:
            nums.append(ele[1])
        return self.lengthOfLIS(nums)

    def lengthOfLIS(self, nums):

        if not nums:
            return 0

        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    cls = Solution()
    print(cls.maxEnveloopes(envelopes))