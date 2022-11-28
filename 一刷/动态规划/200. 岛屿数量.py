class Solution:

    def numIslands(self, grid: list):

        nr = len(grid)
        if nr == 0:
            return 0

        nc = len(grid[0])
        ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    ans += 1
                    grid[r][c] = '0'
                    neighbor = [(r, c)]
                    while neighbor:
                        row, col = neighbor.pop()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbor.append((x, y))
                                grid[x][y] = '0'
        return ans
