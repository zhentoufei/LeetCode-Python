from heapq import *


class MedianFinder:

    # heapq 最小堆
    def __init__(self):
        self.right = []  # 右边小顶堆 A
        self.left = []  # 左边大顶堆 B， 默认该数组会比A多元素一个

    def addNum(self, num: int) -> None:

        if len(self.right) == len(self.left):
            # 加入新数字会变成奇数
            heappush(self.right, num)
            heappush(self.left, -heappop(self.right))
        else:
            # 加入数字会变成偶数
            heappush(self.left, -num)
            heappush(self.right, -heappop(self.left))

    def findMedian(self) -> float:
        return -self.left[0] if len(self.left) != len(self.right) else (self.right[0] - self.left[0]) / 2.0
