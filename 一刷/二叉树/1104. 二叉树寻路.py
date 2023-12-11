class Solution:

    def pathInZigZagTree(self, label: int):
        row = 1
        row_start = 1
        while row_start * 2 <= label:
            row += 1
            row_start *= 2

        if row % 2 == 0:
            # 先转换成正常的label
            label = self.get_reverse(label, row)

        ans = []
        while row > 0:
            if row % 2 == 0:
                ans.append(self.get_reverse(label, row))
            else:
                ans.append(label)
            row -= 1
            label >>= 1

        ans = ans[::-1]
        return ans

    def get_reverse(self, label: int, row: int):
        return (1 << row - 1) + (1 << row) - 1 - label

if __name__ == '__main__':
    s = Solution()
    print(s.pathInZigZagTree(14))