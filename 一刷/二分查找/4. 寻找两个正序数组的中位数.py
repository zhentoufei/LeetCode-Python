class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        size1 = len(nums1)
        size2 = len(nums2)

        left = (size1 + size2 + 1) // 2
        right = (size1 + size2 + 2) // 2
        return (self.getKth(nums1, 0, size1 - 1, nums2, 0, size2 - 1, left)
                + self.getKth(nums1, 0, size1 - 1, nums2, 0, size2 - 1, right)) / 2

    def getKth(self, nums1: list, start1: int, end1: int, nums2: list, start2: int, end2: int, k: int):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)

        if len1 == 0:
            return nums2[start2 + k - 1]

        if k == 1:
            print("start1:{}, start2:{}".format(start1, start2))
            return min(nums1[start1], nums2[start2])

        # 如果k//2 > 数组长度了，就把下标指向数组的最后一位
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    cls = Solution()
    print(cls.findMedianSortedArrays(nums1, nums2))
