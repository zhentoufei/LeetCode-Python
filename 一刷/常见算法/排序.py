import math


class Solution:

    def bubbleSort(self, nums: list):
        '''
        冒泡排序 时间复杂度O(n^2), 空间复杂度O(1)，排序方式In-place， 稳定性排序
        '''
        size = len(nums)
        for i in range(1, len(nums)):
            for j in range(0, size - 1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

    def selectionSort(self, nums: list):
        """
        选择排序 时间复杂度O(n^2)， 空间复杂度O(1)， inplace, 不稳定排序
        首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
        再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        重复第二步，直到所有元素均排序完毕。
        """
        size = len(nums)
        for i in range(size - 1):
            min_index = i
            for j in range(i + 1, size):
                if nums[j] < nums[min_index]:
                    min_index = j
            if i != min_index:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    def insertionSort(self, nums: list):
        """
        插入排序 时间复杂度O(n^2), 空间复杂度O(1), inplace， 稳定排序
        将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
        从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
        （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

        """
        size = len(nums)
        for i in range(size):
            pre_index = i - 1
            current = nums[i]
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index + 1] = nums[pre_index]
                pre_index -= 1
            nums[pre_index + 1] = current
        return nums

    def shellSort(self, nums: list):

        """
        时间复杂度O(nlogn) 空间复杂度O(1) inplace 不稳定
        """
        gap = 1
        size = len(nums)
        while gap < size:
            gap = gap * 2 + 1

        while gap > 0:
            for i in range(gap, size):
                j = i - gap
                temp = nums[i]
                while j >= 0 and nums[j] > temp:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = temp
            gap = gap // 2

        return nums

    def mergeSort(self, nums: list):
        """
        归并排序 O(nlogn) 空间复杂度O(n) 稳定排序

        申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        重复步骤 3 直到某一指针达到序列尾；
        将另一序列剩下的所有元素直接复制到合并序列尾。

        """
        size = len(nums)
        if size < 2:
            return nums

        mid = size // 2
        return self.merge(self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:]))

    def merge(self, left: list, right: list):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while left:
            result.append(left.pop(0))

        while right:
            result.append(right.pop(0))
        return result

    def quickSort(self, nums, left=None, right=None):
        """
        快速排序
        """
        left = 0 if left is None else left
        right = len(nums) - 1 if right is None else right
        if left < right:
            partition_index = self.partition(nums, left, right)
            self.quickSort(nums, left, partition_index - 1)
            self.quickSort(nums, partition_index + 1, right)
        return nums

    def partition(self, nums, left, right):
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
    nums = [3, 1, 3, 3, 2]
    cls = Solution()
    print(cls.quickSort(nums))
