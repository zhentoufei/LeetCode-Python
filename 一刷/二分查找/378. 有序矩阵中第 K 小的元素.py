class Solution:

    def kthSmallest(self, matrix: list, k: int):
        left = matrix[0][0]
        right = matrix[-1][-1]
        rows = len(matrix)
        while left < right:
            mid = (right - left) // 2 + left
            flag, tmp_num = self.check(mid, rows, matrix, k)
            if flag:
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, mid, size, matrix, k):
        i = size - 1
        j = 0
        num = 0
        while i >= 0 and j < size:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1
        return num >= k, num

if __name__ == '__main__':
    matrix = [[1, 6, 6], [6, 6, 12], [12, 13, 15]]
    k = 3
    cls = Solution()
    print(cls.kthSmallest(matrix, k))