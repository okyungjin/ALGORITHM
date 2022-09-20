# Meduim
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List
from collections import Counter

''' [Time Limit Exceeded] Brute Force
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        size = len(nums1)

        for i in range(size):
            for j in range(size):
                k = 0
                while i + k < size and j + k < size and nums1[i + k] == nums2[j + k]:
                    k += 1
                answer = max(answer, k)
        
        return answer

''' Dynamic Programming
Runtime: 4285 ms, faster than 72.66% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 39.2 MB, less than 50.31% of Python3 online submissions for Maximum Length of Repeated Subarray.
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        
        return max(max(row) for row in dp)



solution = Solution()
print(solution.findLength([1,2,3,2,1], [3,2,1,4,7])) # 3
print(solution.findLength([0,0,0,0,0], [0,0,0,0,0])) # 5
print(solution.findLength([0,0,0,0,1], [1,0,0,0,0])) # 4
