class Solution:

    def fun(self, n):
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n = n/2
            else:
                n = (3 * n + 1)/2
            ans += 1
        return ans

if __name__ == '__main__':
    cls = Solution()
    print(cls.fun(10))