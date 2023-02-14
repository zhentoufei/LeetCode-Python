class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode):

        if not root1:
            return root2

        if not root2:
            return root1

        merged = TreeNode(root2.val + root1.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

    def mergeTrees1(self, root1: TreeNode, root2: TreeNode):

        if not root1:
            return root2

        if not root2:
            return root1

        merged_root = TreeNode(root1.val + root2.val)
        queue_merged = [merged_root]
        queue_1 = [root1]
        queue_2 = [root2]
        while queue_1 and queue_2:
            merged = queue_merged.pop(0)
            node1 = queue_1.pop(0)
            node2 = queue_2.pop(0)
            if node1.left or node2.left:
                if node1.left and node2.left:
                    merged.left = TreeNode(node1.left.val + node2.left.val)
                    queue_merged.append(merged.left)
                    queue_1.append(node1.left)
                    queue_2.append(node2.left)
                elif node1.left:
                    merged.left = node1.left
                else:
                    merged.left = node2.left

            if node1.right or node2.right:
                if node1.right and node2.right:
                    merged.right = TreeNode(node1.right.val + node2.right.val)
                    queue_merged.append(merged.right)
                    queue_1.append(node1.right)
                    queue_2.append(node2.right)
                elif node1.right:
                    merged.right = node1.right
                else:
                    merged.right = node2.right
        return merged_root

if __name__ == '__main__':
    t1 = TreeNode(1)
    t11 = TreeNode(3)
    t1.left = t11
    t2 = TreeNode(2)
    t22 = TreeNode(1)
    t2.left = t22
    cls = Solution()
    print(cls.mergeTrees1(t1, t2))