# Medium
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1: return range(10)
        
        iter_nums = range(1, 10)

        for i in range(n - 1):
            next_iter_nums = []
            for num in iter_nums:
                for next_num in set([num % 10 + k, num % 10 - k]):
                    if 0 <= next_num < 10:
                        next_iter_nums.append(num * 10 + next_num)
            iter_nums = next_iter_nums
        
        return iter_nums




solution = Solution()
print(solution.numsSameConsecDiff(3, 7)) # [181,292,707,818,929]
print(solution.numsSameConsecDiff(1, 1)) # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]