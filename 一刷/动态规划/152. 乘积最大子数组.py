class Solution:

    def maxProduct(self, nums: list):
        if not nums:
            return 0

        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]: # 注意这里的是从第二个元素开始的
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res