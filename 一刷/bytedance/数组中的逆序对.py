class Solution:
    def reversePairs(self, record: list) -> int:
        temp = [0] * len(record)
        return self.merge_sort(0, len(record) - 1, record, temp)

    def merge_sort(self, left, right, record: list, temp: list):
        if left >= right:
            return 0
        # 递归划分
        mid = left + (right - left) // 2
        sub_merge_count = self.merge_sort(left, mid, record, temp) + self.merge_sort(mid + 1, right, record, temp)
        merge_count = self.merge_and_count(left, mid, right, record, temp)
        return sub_merge_count + merge_count

    def merge_and_count(self, left, mid, right, record, temp):
        # 合并阶段
        i = left
        j = mid + 1
        ans = 0
        temp[left:right + 1] = record[left:right + 1]
        for k in range(left, right + 1):
            if i == mid + 1:
                # 当左边数组遍历完成
                record[k] = temp[j]
                j += 1
            elif j == right + 1:
                # 当右边数组遍历完成
                record[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                # 当没有超出两个数组的范围，仅仅是，稳定的排序
                record[k] = temp[i]
                i += 1
            else:
                # 右边数组开始放入到对应的数组中
                record[k] = temp[j]
                j += 1
                ans += mid - i + 1  # 统计逆序对
        return ans
