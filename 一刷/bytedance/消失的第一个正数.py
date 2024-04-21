'''
1..n 连续正整数list，随机拿掉一个数字k，然后进行shuffle，返回k
input：[2,5,7,1,4,3]
output: 6
'''


def find_miss_one(nums: list):
    num_sum = sum(nums)
    size = len(nums)
    size_sum = (1 + size + 1) * (size + 1) // 2
    return size_sum - num_sum


# print(find_miss_one([2, 5, 7, 1, 4, 3]))

'''
未排序的数组，找出没有出现的最小正整数
'''


def first_miss_pos(nums: list):
    size = len(nums)
    for i in range(size):
        if nums[i] <= 0:
            nums[i] = size + 1

    for i in range(size):
        num = abs(nums[i])
        if num <= size:
            nums[num - 1] = -1 * abs(nums[num - 1])

    for i in range(size):
        if nums[i] > 0:
            return i + 1
    return size + 1


# print(first_miss_pos([-7, -9, -1, 0, 1, 9]))

'''
给定一个数组，包含从1到N的所有的整数，但是其中缺了两个数字，您能在O(n)时间内，O(1)的空间内，找到他们么？
'''


def find_miss_two(nums: list):
    full_size = len(nums) + 2
    two_sum = (1 + full_size) * full_size // 2 - sum(nums)
    half_size = two_sum // 2
    small_miss_one = (1 + half_size) * half_size // 2 - sum([x for x in nums if x <= half_size])
    return [small_miss_one, two_sum - small_miss_one]


print(find_miss_two([1, 3]))
