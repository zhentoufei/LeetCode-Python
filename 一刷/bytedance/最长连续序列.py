class Solution:
    def longestConsecutive(self, nums: list) -> int:

        num_set = set(nums)
        ans = 0
        for ele in nums:

            if ele - 1 not in num_set:
                current = ele
                counter = 1
                while current + 1 in num_set:
                    current += 1
                    counter += 1

                ans = max(ans, counter)
        return ans
