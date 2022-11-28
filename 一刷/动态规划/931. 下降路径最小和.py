class Solution:

    def minFallingPathSum(self, matrix: list):
        row_num = len(matrix)
        col_num = len(matrix[0])

        dp = [[float('inf') for _ in range(col_num)] for _ in range(row_num)]

        for row_index in range(row_num):
            for col_index in range(col_num):

                if row_index == 0:
                    dp[row_index][col_index] = matrix[row_index][col_index]
                else:
                    if col_index - 1 >= 0:
                        dp[row_index][col_index] = min(dp[row_index][col_index], dp[row_index - 1][col_index - 1] + matrix[row_index][col_index])

                    dp[row_index][col_index] = min(dp[row_index][col_index], dp[row_index - 1][col_index] + matrix[row_index][col_index])

                    if col_index + 1 <= col_num - 1:
                        dp[row_index][col_index] = min(dp[row_index][col_index], dp[row_index - 1][col_index + 1] + matrix[row_index][col_index])


        return min(dp[-1])
