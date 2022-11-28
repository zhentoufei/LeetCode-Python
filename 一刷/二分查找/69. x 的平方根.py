class Solution:

    def mySqrt(self, n: int):
        left = 0
        right = n
        while left <= right:
            mid = (right - left) // 2 + left
            if n == mid * mid:
                return mid
            elif n > mid * mid:
                left = mid + 1
            elif n < mid * mid:
                right = mid - 1
        return left - 1

if __name__ == '__main__':
    cls = Solution()
    print(cls.mySqrt(5))