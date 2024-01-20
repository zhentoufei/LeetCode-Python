class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    a = [2, 4, 1]
    for i, j in enumerate(a):
        print(f'i:{i}, j:{j}')
