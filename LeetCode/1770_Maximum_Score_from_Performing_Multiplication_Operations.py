# Medium
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

from typing import List
from collections import deque

''' Dynamic Programming
Runtime: 7649 ms, faster than 60.77% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
Memory Usage: 23.2 MB, less than 97.48% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
'''
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        dp = [0] * (m + 1)

        for i in range(m - 1, -1, -1):
            d = [0] * (i + 1)
            for j in range(i, -1, -1):
                d[j] = max(dp[j + 1] + multipliers[i] * nums[j], dp[j] + multipliers[i] * nums[~(i - j)])
            dp = d
        
        return dp[0]


solution = Solution()
print(solution.maximumScore([1,2,3], [3, 2, 1])) # 14
print()
print(solution.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6])) # 102
