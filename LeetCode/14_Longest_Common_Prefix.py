# Easy
# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        if len(strs) == 2: return self.getCommonStr(strs[0], strs[1])

        common_str = self.getCommonStr(strs[0], strs[1])
        for i in range(2, len(strs)):
            common_str = self.getCommonStr(common_str, strs[i])

        return common_str
            

    def getCommonStr(self, a: str, b: str) -> str:
        min_len = min(len(a), len(b))

        res = ''
        for i in range(min_len):
            if a[i] != b[i]: return res    
            res += a[i]

        return res
            


solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))

        