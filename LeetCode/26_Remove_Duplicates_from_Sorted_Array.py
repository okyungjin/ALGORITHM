# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

# sol1) 22.08.10
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
    
        return left + 1
            


solution = Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))