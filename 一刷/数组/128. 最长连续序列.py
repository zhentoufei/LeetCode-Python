class Solution:

    def longestConsecutive(self, nums: list):

        num_set = set(nums)
        ans = 0

        for ele in nums:
            if ele - 1 not in num_set:
                current_num = ele
                res = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    res += 1
                ans = max(ans, res)
        return ans