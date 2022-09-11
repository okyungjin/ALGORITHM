# Hard
# https://leetcode.com/problems/maximum-performance-of-a-team/

from typing import List, Iterable, Tuple
from heapq import heappush, heappop

'''
Runtime: 1045 ms, faster than 5.49% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 29.6 MB, less than 83.54% of Python3 online submissions for Maximum Performance of a Team.
'''
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        candiates = sorted(zip(efficiency, speed), reverse=True)
        cur_sum = max_perf = 0
        heap = []
        
        for _efficiency, _speed  in candiates:
            while len(heap) > k - 1:
                cur_sum -= heappop(heap)
            heappush(heap, _speed)
            cur_sum += _speed
            max_perf = max(max_perf, cur_sum * _efficiency)
            
        return max_perf % MOD


solution = Solution()
print(solution.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)) # 60
# print(solution.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3)) # 68
# print(solution.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4)) # 72


