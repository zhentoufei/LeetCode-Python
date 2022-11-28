class Solution:

    def checkInclusion(self, s1: str, s2: str):

        need = {}
        window = {}

        for ele in s1:
            if ele not in need.keys():
                need[ele] = 0
            need[ele] += 1

        left = 0
        right = 0
        valid = 0

        while right < len(s2):

            move_in = s2[right]
            right += 1
            if move_in in need.keys():
                if move_in not in window.keys():
                    window[move_in] = 0
                window[move_in] += 1

                if window[move_in] == need[move_in]:
                    valid += 1

            while right - left >= len(s1):

                if valid == len(need):
                    return True

                move_out = s2[left]
                left += 1
                if move_out in need.keys():
                    if window[move_out] == need[move_out]:
                        valid -= 1
                    window[move_out] -= 1

        return False

if __name__ == '__main__':
    s1 = 'ab'
    s2 = "eidbaooo"
    cls = Solution()
    print(cls.checkInclusion(s1, s2))