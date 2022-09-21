# Meduim
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        evenSum = self.getEvenSum(nums)
        
        for val, i in queries:
            if self.isEven(nums[i]): 
                evenSum -= nums[i]    
            nums[i] += val
            if self.isEven(nums[i]):
                evenSum += nums[i]
            answer.append(evenSum)

        return answer
    

    def getEvenSum(self, nums: List[int]) -> int:
        evenSum = 0
        for num in nums:
            if self.isEven(num): evenSum += num
                
        return evenSum
    

    def isEven(self, num: int) -> bool:
        return num % 2 == 0


solution = Solution()
print(solution.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])) # [8,6,2,4]
print(solution.sumEvenAfterQueries([1], [[4,0]])) # [0]
