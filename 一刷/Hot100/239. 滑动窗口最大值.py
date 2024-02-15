class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_flag = False  # 行是否有0
        col_flag = False  # 列是否有0
        for i in range(col):
            if matrix[0][i] == 0:
                row_flag = True
                break

        for i in range(row):
            if matrix[i][0] == 0:
                col_flag = True
                break

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if col_flag:
            for j in range(row):
                matrix[j][0] = 0

        if row_flag:
            for i in range(col):
                matrix[0][i] = 0
        return matrix

if __name__ == '__main__':
    matrix = [[1,0,3]]
    so = Solution()
    print(so.setZeroes(matrix))