'''
无序数组的中位数
方法1：排序找中位数
方法2：快速排序找中位数
方法3：最小堆找中位数
'''


def sort_and_mid(nums: list):
    size = len(nums)
    if nums is None or len(nums) == 0:
        return -1

    nums = sorted(nums)
    mid = size // 2
    if size % 2 == 0:
        return (nums[mid] + nums[mid - 1]) / 2.
    else:
        return mid


def partition_and_mid(nums: list):
    if not nums:
        return -1
    size = len(nums)
    mid = size // 2
    if size % 2 == 1:
        return get_num(nums, mid)
    else:
        return (get_num(nums, mid) + get_num(nums, mid - 1)) / 2.


def get_num(nums, mid):
    left = 0
    right = len(nums) - 1
    index = -1
    while index != mid:
        index = partition(nums, left, right)
        if index > mid:
            right = index - 1
        elif index < mid:
            left = index + 1
        else:
            break
    return nums[index]


def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    i = pivot + 1

    while i <= right:
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
        i += 1
    nums[pivot], nums[index - 1] = nums[index - 1], nums[pivot]
    return index - 1


if __name__ == '__main__':
    nums = [10, 2, 3]
    print(partition_and_mid(nums))
