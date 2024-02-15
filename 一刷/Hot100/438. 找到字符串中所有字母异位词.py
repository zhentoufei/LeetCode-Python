class Solution:

    def findAnagrams(self, s: str, p: str):
        need = {}
        window = {}
        ans = []

        for ele in p:
            if ele not in need.keys():
                need[ele] = 0
            need[ele] += 1

        left = 0
        right = 0
        valid = 0

        while right < len(s):
            move_in = s[right]
            right += 1

            if move_in in need.keys():
                if move_in not in window.keys():
                    window[move_in] = 0
                window[move_in] += 1

                if need[move_in] == window[move_in]:
                    valid += 1

            while right - left >= len(p):

                if valid == len(need):
                    ans.append(left)

                move_out = s[left]
                left += 1
                if move_out in need.keys():
                    if window[move_out] == need[move_out]:
                        valid -= 1
                    window[move_out] -= 1
        return ans

if __name__ == '__main__':
    so = Solution()
    s = "baa"
    p = "aa"
    print(so.findAnagrams(s, p))
