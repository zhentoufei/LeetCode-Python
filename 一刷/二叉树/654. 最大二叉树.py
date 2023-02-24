class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def constructMaximumBinaryTree(self, nums:list):
        return self.build(nums, 0, len(nums) - 1)

    def build(self, num: list, left: int, right: int):
        if left > right:
            return None

        max_index = self.find_max_index(num, left, right)
        node = TreeNode(num[max_index])
        node.left = self.build(num, left, max_index - 1)
        node.right = self.build(num, max_index + 1, right)
        return node

    def find_max_index(self, num: list, left: int, right: int):
        max_index = left
        for i in range(left + 1, right + 1, 1):
            if num[i] > num[max_index]:
                max_index = i

        return max_index

    def constructMaximumBinaryTree_v1(self, nums:list):
        queue = []

        for ele in nums:
            current_node = TreeNode(ele)
            while queue:
                last_node = queue[-1]
                if current_node.val < last_node.val:
                    last_node.right = current_node
                    queue.append(current_node)
                    break
                else:
                    queue.pop()
                    current_node.left = last_node

            if not queue:
                queue.append(current_node)

        return queue[0]

















