# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = dict.fromkeys(nums)
        
        for i in range(len(nums)):
            if not i in num_dict: return i

        return i + 1

# TEST
solution = Solution()

print(solution.missingNumber([3,0,1]))
print(solution.missingNumber([0,1]))
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))