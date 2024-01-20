import collections


class Solution:

    def groupAnagrams(self, strs):

        memo  = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            memo[key].append(str)

        return list(memo.values())