# Easy
# https://leetcode.com/problems/contains-duplicate/

'''
Runtime: 610 ms, faster than 64.91% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.8 MB, less than 96.55% of Python3 online submissions for Contains Duplicate.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        alreadyExist = dict()
        
        for num in nums:
            if num in alreadyExist: return True
            alreadyExist[num] = 1
        
        return False