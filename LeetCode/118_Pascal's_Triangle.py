# Easy
# https://leetcode.com/problems/pascals-triangle/

from typing import List

'''
Runtime: 53 ms, faster than 35.11% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.8 MB, less than 65.59% of Python3 online submissions for Pascal's Triangle.
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1], [1, 1]]

        if numRows == 1: return [[1]]
        if numRows == 2: return pascalTriangle

        for i in range(2, numRows):
            triangle = []
            prevTriangle = pascalTriangle[i - 1]

            for j in range(len(prevTriangle) - 1):
                triangle.append(prevTriangle[j] + prevTriangle[j + 1])

            pascalTriangle.append([1] + triangle + [1])

        return pascalTriangle



solution = Solution()

''' TestCase #1
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
print(solution.generate(5))

''' TestCase #2
Input: numRows = 1
Output: [[1]]
'''
print(solution.generate(1))