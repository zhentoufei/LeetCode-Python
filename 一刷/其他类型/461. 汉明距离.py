class Solution:

    def hammingDistance(self, x:int, y:int):
        s = x ^ y
        ans = 0
        while s != 0:
            s &= (s - 1)
            ans += 1

        return ans
