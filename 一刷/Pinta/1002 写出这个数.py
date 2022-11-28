class Solution:

    def fun(self, n: str):
        pinyin = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
        agg = 0
        for i in range(len(n)):
            agg += ord(n[i]) - ord('0')

        num_list = []  # 栈
        while agg > 0:
            num_list.append(agg % 10)
            agg = agg // 10

        ans = []
        while num_list:
            a = num_list.pop()
            ans.append(pinyin[a])
        return ' '.join(ans)


if __name__ == '__main__':
    cls = Solution()
    print(cls.fun('123123'))
