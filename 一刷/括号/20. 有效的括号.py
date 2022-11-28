class Solution:

    def isValid(self, s: str):
        info = {']': '[', '}': '{', ')': '('}
        tmp = []

        for i in s:
            if len(tmp) == 0 or i not in info.keys():
                tmp.append(i)

            if i in info.keys() and info[i] != tmp[-1]:
                return False

            if i in info.keys() and info[i] == tmp[-1]:
                tmp.pop()

        if len(tmp) > 0:
            return False
        return True
