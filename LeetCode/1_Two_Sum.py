# [Easy] https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    # 1차 풀이 (22.08.05)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = { num: idx for idx, num in enumerate(nums)}

        for idx, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in nums_dict:
                if idx == nums_dict[second_num]: continue
                return [idx, nums_dict[second_num]]

class Solution:
    # 2차 풀이 (22.08.05)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            another = target - num

            if another in seen: 
                return [seen[another], idx]
            seen[num] = idx


solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3, 3], 6))
print(solution.twoSum([3, 2, 4], 6)) # [1, 2]