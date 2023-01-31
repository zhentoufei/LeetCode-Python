class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    https://leetcode.cn/problems/path-sum-iii/solution/dui-qian-zhui-he-jie-fa-de-yi-dian-jie-s-dey6/
    '''

    def pathSum(self, root: TreeNode, targetSum: int):
        self.prefix_map = {}  # key是前缀和, value是大小为key的前缀和出现的次数
        self.target = targetSum
        self.prefix_map[0] = 1  # 前缀和为0的一条路径
        return self.rec(root, 0)  # 前缀和的递归回溯思路

    def rec(self, node: TreeNode, cur_sum: int):
        """

        :param node:
        :param cur_sum:
        :return:
        """
        if not node:
            return 0
        ans = 0
        cur_sum += node.val
        if cur_sum - self.target not in self.prefix_map.keys():
            self.prefix_map[cur_sum - self.target] = 0
        ans += self.prefix_map[cur_sum - self.target]

        if cur_sum not in self.prefix_map.keys():
            self.prefix_map[cur_sum] = 0
        self.prefix_map[cur_sum] += 1

        left = self.rec(node.left, cur_sum)
        right = self.rec(node.right, cur_sum)
        ans = ans + left + right
        self.prefix_map[cur_sum] -= 1
        return ans

if __name__ == '__main__':
    cls = Solution()
    tr1 = TreeNode(1)
    print(cls.pathSum(tr1, 0))