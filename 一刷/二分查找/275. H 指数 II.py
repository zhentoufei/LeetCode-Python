class Solution:
    '''
    对于下标 i（满足它左侧的元素小于它），引用次数 >=citations[i] 的有 N-i 篇。即这 N-i 篇的引用次数 >= citations[i]。
    即对于citations[i]，h指数是 N-i 。
    要找到最大的 N-i （即最小的 i ），使 citations[i]>=N-i（保证满足条件的论文 >=N-i 篇） -> i+citations[i]>=N。
    又由于 i+citations[i] 递增，可以使用二分法搜索 i 。
    '''
    def hIndex(self, citations: list):
        left = 0
        size = len(citations)
        right = size - 1
        while left <= right:

            mid = (right - left) // 2 + left
            if citations[mid] >= size - mid:
                right = mid - 1
            else:
                left = mid + 1
        return size - left
