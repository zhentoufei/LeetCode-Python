'''
[ 1 11 15 21
  31 65 78 4
  97 11 18 63
]

[1 11 31 97 65 15 21 78 11 18 4 63]
'''


def printInOneDim(mat: list):
    ans = []
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows + cols - 1):

        if i % 2:
            # 向上
            x = 0 if i < cols else i - cols + 1
            y = i if i < cols else cols - 1
            while x < rows and y >= 0:
                ans.append(mat[x][y])
                x += 1
                y -= 1
        else:
            # 向下
            x = i if i < rows else rows - 1
            y = 0 if i < rows else i - rows + 1
            while x >= 0 and y < cols:
                ans.append(mat[x][y])
                x -= 1
                y += 1
    return ans


if __name__ == '__main__':
    dim_2 = [[1, 11, 15, 21], [31, 65, 78, 4], [97, 11, 18, 63]]
    print(printInOneDim(dim_2))
