class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return []
        ans = None
        p_path = self.getPath(root, p)
        q_path = self.getPath(root, q)
        for ele_p, ele_q in zip(p_path, q_path):
            if ele_p == ele_q:
                ans = ele_p
            else:
                break
        return ans

    def getPath(self, root: TreeNode, target: TreeNode):
        path = []
        node = root
        while node != target:
            path.append(node)
            if node.val > target.val:
                node = node.left
            else:
                node = node.right
        path.append(node)

        return path

class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        ans = root
        while True:
            if ans.val > p.val and ans.val > q.val:
                ans = ans.left
            elif ans.val < p.val and ans.val < q.val:
                ans = ans.right
            else:
                break
        return ans


