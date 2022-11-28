class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_arr = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted_arr.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted_arr.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted_arr.append(nums1[p1])
                p1 += 1
            else:
                sorted_arr.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted_arr
