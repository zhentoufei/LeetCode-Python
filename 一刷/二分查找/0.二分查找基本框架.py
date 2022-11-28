# https://blog.csdn.net/qq_41221520/article/details/108277801

class Solution:
    # 查找某个值

    def binarySearch(self, nums: list, target: int):
        size = len(nums)
        left = 0
        right = size - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # 查找第一个大于（大于等于） target 的值
    def binarySearchBigger(self, nums: list, target: int):
        size = len(nums)
        left = 0
        right = size - 1

        while left <= right:
            mid = left + (right - left) // 2
            # 下面是求大于 target的值，如果是大于等于，只需要将 if 里的判断条件改为 if(array[mid] < target) 即可。
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 查找第一个小于（小于等于） target 的值
    def binarySearchSmaller(self, nums: list, target: int):
        size = len(nums)
        left = 0
        right = size - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 下面是求小于的值，如果小于等于，只需要将 if 里的判断条件改为 if(array[mid] > target) 即可。
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    cls = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6]
    target = 2
    print(cls.binarySearchBigger(nums, target))
