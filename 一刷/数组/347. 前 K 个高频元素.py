import heapq


class Solution:

    def topKFrequent(self, nums: list, k: int):

        dict_value = {}
        for i in nums:

            if i in dict_value:
                dict_value[i] += 1
            else:
                dict_value[i] = 1

        heap_list = []
        for key, value in dict_value.items():
            if len(heap_list) < k:
                heapq.heappush(heap_list, (value, key))
                print(heap_list)
            elif value > heap_list[0][0]:
                heapq.heapreplace(heap_list, (value, key))

        ans = []
        while heap_list:
            ans.append(heapq.heappop(heap_list)[1])
        return ans


if __name__ == '__main__':
    cls = Solution()
    nums = [1, 1, 3, 1, 2, 2]
    k = 2
    print(cls.topKFrequent(nums, k))
