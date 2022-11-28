class Solution:

    def strStr(self, haystack: str, needle: str):
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        #  增加空格，从下标1 开始
        haystack = " " + haystack
        needle = " " + needle

        # 构建 next 数组，数组长度为匹配串的长度（next 数组是和匹配串相关的）
        next = [0] * (m + 1)
        j = 0
        for i in range(2, m + 1):
            # 匹配不成功的话，j = next(j)
            while j > 0 and needle[i] != needle[j + 1]:
                j = next[j]

            # 匹配成功
            if needle[i] == needle[j + 1]:
                j += 1

            # 更新next[i]
            next[i] = j
        # 匹配过程，i = 1，j = 0 开始，i 小于等于原串长度 【匹配 i 从 1 开始】
        j = 0
        for i in range(1, n + 1):

            # 匹配不成功 j = next(j)
            # while (j > 0 & & s[i] != p[j + 1]) j = next[j];
            while j > 0 and haystack[i] != needle[j + 1]:
                j = next[j]

            # 匹配成功的话，先让j + +，结束本次循环后i + +
            if haystack[i] == needle[j + 1]:
                j += 1
            # 整一段匹配成功，直接返回下标
            if j == m:
                return i - m
        return -1

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"

    cls = Solution()
    print(cls.strStr(haystack, needle))