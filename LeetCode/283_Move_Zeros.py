# Easy
# https://leetcode.com/problems/move-zeroes/

from typing import List

# sol1) 22.08.09
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] == 0:
                if nums[p2] == 0:
                    p2 += 1
                    continue
            else:
                p1 += 1
                p2 += 1
                continue

            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1


            
            


        
            
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([0]))