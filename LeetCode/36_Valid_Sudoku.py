# https://leetcode.com/problems/valid-sudoku/

from typing import List

BOARD_SIZE = 9


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check validation by row
        for row in board:
            dic = {}
            for elem in row:
                if elem == '.': continue
                if elem in dic: return False
                else: dic[elem] = 1
        
        # check validation by column
        for i in range(BOARD_SIZE):
            dic = {}
            for j in range(BOARD_SIZE):
                elem = board[j][i]
                if elem == '.': continue
                if elem in dic: return False
                else: dic[elem] = 1

        # check validation by sub-box
        sub_box_start_points = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for (i, j) in sub_box_start_points:
            dic = {}
            range_i = [i for i in range(i, i + 3)]
            range_j = [j for j in range(j, j + 3)]
            
            for x in range_i:
                for y in range_j:
                    elem = board[x][y]
                    if elem == '.': continue
                    if elem in dic: return False
                    else: dic[elem] = 1
        return True
    

# TEST
solution = Solution()

print(solution.isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])) # True


print(solution.isValidSudoku([
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])) # False


print(solution.isValidSudoku([
    [".",".","5",".",".",".",".",".","."],
    [".",".",".","8",".",".",".","3","."],
    [".","5",".",".","2",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","9"],
    [".",".",".",".",".",".","4",".","."],
    [".",".",".",".",".",".",".",".","7"],
    [".","1",".",".",".",".",".",".","."],
    ["2","4",".",".",".",".","9",".","."]
])) # False