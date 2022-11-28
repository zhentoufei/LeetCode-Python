class Solution:

    def hIndex(self, citations: list):

        size = len(citations)
        memo = [0] * (size + 1)
        for ci in citations:
            if ci >= size:
                memo[size] += 1
            else:
                memo[ci] += 1
        total = 0
        for i in range(size, -1, -1):
            total += memo[i]
            if total >= i:
                return i
        return 0