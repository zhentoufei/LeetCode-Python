class Solution:

    def __init__(self):
        self.direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board: list, word: str):
        rows = len(board)
        cols = len(board[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if self.check(i, j, 0, board, word, visited):
                    return True
        return False

    def check(self, i: int, j: int, k: int, board: list, word: str, visited: set):

        if board[i][j] != word[k]:
            return False

        if len(word) - 1 == k:
           return True

        visited.add((i, j))
        ans = False

        for di, dj in self.direction:
            newi, newj = di + i, dj + j
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and (newi, newj) not in visited:
                if self.check(newi, newj, k + 1, board, word, visited):
                    ans = True
                    break
        visited.remove((i, j))
        return ans
