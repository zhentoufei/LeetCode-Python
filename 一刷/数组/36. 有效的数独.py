class Solution:

    def isValidSudoku(self, board: list):
        # 哈希表存储每一行的每个数是否出现过，默认初始情况下，每一行每一个数都没有出现过
        # 整个board有9行，第二维的维数10是为了让下标有9，和数独中的数字9对应。
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]  # 存储每一列的每个数是否出现过，默认初始情况下，每一列的每一个数都没有出现过
        # 存储每一个box的每个数是否出现过，默认初始情况下，在每个box中，每个数都没有出现过。整个board有9个box
        box = [[0] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                current = ord(board[i][j]) - ord('0')
                if row[i][current] > 0:
                    return False

                if col[j][current] > 0:
                    return False

                if box[j // 3 + (i // 3) * 3][current] > 0:
                    return False

                # 之前都没出现过，现在出现了，就给它置为1，下次再遇见就能够直接返回false了
                row[i][current] = 1
                col[j][current] = 1
                box[j // 3 + i // 3 * 3][current] = 1
        return True
