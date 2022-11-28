class Solution:

    def searchMatrix(self, matrix: list, target: int):
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            mid = (right - left) // 2 + left
            current = matrix[mid // col][mid % col]
            if current == target:
                return True
            elif current < target:
                left = mid + 1
            elif current > target:
                right = mid - 1
        return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    cls = Solution()
    print(cls.searchMatrix(matrix, target))
