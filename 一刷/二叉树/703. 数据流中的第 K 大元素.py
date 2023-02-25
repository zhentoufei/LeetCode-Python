import heapq


class KthLargest(object):

    def __init__(self, k:int, nums: list):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int):
        '''
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]

        '''

        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]