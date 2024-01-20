class Solution:

    def longestConsecutive(self, nums):
        ans = 0
        if len(nums) == 0:
            return 0
        memo_set = set()
        for i in nums:
            memo_set.add(i)

        for i in nums:

            current = 0
            if i - 1 not in memo_set:
                while i in memo_set:
                    current += 1
                    i += 1

                ans = max(current, ans)

        return ans

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    s = Solution()
    print(s.longestConsecutive(nums))
