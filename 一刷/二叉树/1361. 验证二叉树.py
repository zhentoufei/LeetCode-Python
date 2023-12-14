import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: list, rightChild: list):

        indeg = [0] * n
        for u in leftChild:
            if u != -1:
                indeg[u] += 1
        for u in rightChild:
            if u != -1:
                indeg[u] += 1


        root = -1
        for i in range(n):
            if indeg[i] == 0:
                root = i
                break
        if root == -1:
            return False

        seen = set([root])
        q = collections.deque([root])
        while len(q) > 0:
            u = q.popleft()
            if leftChild[u] != -1:
                if leftChild[u] in seen:
                    return False
                seen.add(leftChild[u])
                q.append(leftChild[u])

            if rightChild[u] != -1:
                if rightChild[u] in seen:
                    return False
                seen.add(rightChild[u])
                q.append(rightChild[u])

        return len(seen) == n

if __name__ == '__main__':
    s = Solution()
    print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))