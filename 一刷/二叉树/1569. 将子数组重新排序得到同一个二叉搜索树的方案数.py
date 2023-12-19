class TNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.size = 1
        self.ans = 0


class Solution:
    def numOfWays(self, nums: list) -> int:
        def insert(val: int):
            cur = root
            while True:
                cur.size += 1
                if val < cur.value:
                    if not cur.left:
                        cur.left = TNode(val)
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = TNode(val)
                        return
                    cur = cur.right

        def dfs(node: TNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1
            node.ans = c[lsize + rsize][lsize] * lans * rans % mod

        n = len(nums)
        if n == 1:
            return 0

        mod = 10 ** 9 + 7
        c = [[0] * n for _ in range(n)]
        c[0][0] = 1
        for i in range(1, n):
            c[i][0] = 1
            for j in range(1, n):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

        root = TNode(nums[0])
        for i in range(1, n):
            val = nums[i]
            insert(val)

        dfs(root)
        return (root.ans - 1 + mod) % mod
