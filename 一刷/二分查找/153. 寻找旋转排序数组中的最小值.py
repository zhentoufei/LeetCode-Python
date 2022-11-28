class Solution:
    def findMin(self, nums: list):
        low, high = 0, len(nums) - 1
        while low <= high: # 在区间 [low, high] 内进行查找
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]: # 说明，[pivot, high] 里面的数字是恒大于等于 num[pivot]的，在右半边的数组中
                high = pivot - 1 # 区间缩小到 [low, pivot - 1]
            else:  # 如果 nums[pivot] >= nums[high]，说明pivot 在左半边的数组中
                low = pivot + 1 # 区间缩小到 [pivot + 1, high]
        return nums[low]

if __name__ == '__main__':
    cls = Solution()
    print(cls.findMin([3, 1, 2]))
