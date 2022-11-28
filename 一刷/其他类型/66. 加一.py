class Solution:

    def plusOne(self, digits: list):
        size = len(digits)
        for i in range(size - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        ans = [0] * (size + 1)
        ans[0] = 1
        return ans


if __name__ == '__main__':
    digits = [1, 2, 9, 1]
    cls = Solution()
    print(cls.plusOne(digits))
