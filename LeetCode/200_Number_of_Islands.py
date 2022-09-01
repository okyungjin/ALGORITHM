# Meduim
# https://leetcode.com/problems/number-of-islands/

'''
1 ISLAND
0 WATER
'''

from typing import List

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.search_island(grid, x, y):
                    island_count += 1
        
        return island_count


    def search_island(self, grid: List[List[str]], x: int, y: int):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]): return False
        if grid[x][y] == '0': return False
        
        # mark visited
        grid[x][y] = '0'

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            self.search_island(grid, nx, ny)

        return True

        

solution = Solution()
print(solution.numIslands([
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
])) # 1
print(solution.numIslands([
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
])) # 3
