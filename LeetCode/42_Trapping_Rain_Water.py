from typing import List

''' [Memory Limit Exceeded] '''
class Solution:
    def trap(self, height: List[int]) -> int:
        size, maxHeight = len(height), max(height)
        maps = [[0] * size for _ in range(maxHeight)]
        water = 0
        
        for i in range(size):
            for j in range(height[i]):
                maps[j][i] = 1
                
        for i in range(maxHeight):
            for j in range(size):
                if maps[i][j] == 1:
                    for l in range(j + 1, size):
                        if maps[i][l] == 1:
                            water += max(l - j - 1, 0)
                            j = l + 1
                            break
        return water

''' Two Pointers
Runtime: 313 ms, faster than 13.21% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 15.9 MB, less than 81.24% of Python3 online submissions for Trapping Rain Water.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1 # two pointers
        lowest, highest = 0, 0
        
        while left <= right:
            lower = min(height[left], height[right])
            highest = max(lower, highest)
            
            water += highest - lower
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return water
         
                        

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(solution.trap([4,2,0,3,2,5])) # 9
