# Meduim
# https://leetcode.com/problems/rotate-image/

from typing import List

# sol1) 22.08.31
# not in-place
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        origin_matrix = [row[:] for row in matrix]

        for col_idx in range(n):
            row = []
            for row_idx in range(n - 1, -1, -1):
                row.append(origin_matrix[row_idx][col_idx])
            matrix[col_idx] = row


# sol2) 22.09.01
# in-place
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        if isEven(n): y_range = (n + 1) // 2
        else:         y_range = n // 2
        
        for x in range((n + 1) // 2):
            for y in range(y_range):
                start = matrix[x][y]

                matrix[x][y] = matrix[n-1-y][x]
                matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
                matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
                matrix[y][n-1-x] = start


def isEven(n: int) -> bool: return n % 2 == 0

   
solution = Solution()
print(solution.rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
print(solution.rotate([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


    