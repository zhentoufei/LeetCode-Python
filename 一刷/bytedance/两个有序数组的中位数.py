class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        size_1 = len(nums1)
        size_2 = len(nums2)

        if size_1 > size_2:
            return self.findMedianSortedArrays(nums2, nums1)

        i_min = 0
        i_max = size_1
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = (size_1 + size_2 + 1) // 2 - i

            if i != size_1 and j != 0 and nums1[i] < nums2[j - 1]:
                # nums1[i] > nums2[j - 1]
                i_min = i + 1
            elif i != 0 and j != size_2 and nums1[i - 1] > nums2[j]:
                # nums1[i-1] > nums2[j]
                i_max = i - 1
            else:
                max_left = 0
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (size_1 + size_2) % 2 == 1:
                    return max_left

                min_right = 0
                if i == size_1:
                    min_right = nums2[j]
                elif j == size_2:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2
        # return 0
