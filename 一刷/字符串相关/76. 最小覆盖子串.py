class Solution:

    def minWindow(self, s: str, t: str):

        need = {}
        window = {}

        for ele in t:
            if ele not in need.keys():
                need[ele] = 0
            need[ele] += 1

        left = 0
        right = 0
        valid = 0
        length = float('inf')
        start = 0
        while right < len(s):

            move_in = s[right]
            right += 1
            if move_in in need.keys():
                if move_in not in window.keys():
                    window[move_in] = 0
                window[move_in] += 1

                if window[move_in] == need[move_in]:
                    valid += 1

                while valid == len(need):
                    if right - left < length:
                        start = left
                        length = right - left

                    move_out = s[left]
                    left += 1
                    if move_out in need.keys():
                        if need[move_out] == window[move_out]:
                            valid -= 1
                        window[move_out] -= 1

        return s[start: start + length] if length < float('inf') else ""


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    cls = Solution()
    print(cls.minWindow(s, t))
