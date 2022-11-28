class Solution:

    def revers(self, x: int):
        ans = 0
        flag = 1
        if x < 0:
            flag = -1
            x = x * -1

        while x != 0:
            tmp = x % 10
            if ans > 2 ** 31 // 10 or (ans == 2 ** 31 // 10 and tmp >= 8):
                return 0
            ans = ans * 10 + tmp
            x = x // 10
        return ans * flag


if __name__ == '__main__':
    cls = Solution()
    print(cls.revers(-123))
