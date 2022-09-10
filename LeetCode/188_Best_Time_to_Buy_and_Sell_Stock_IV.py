# Hard
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from typing import List

''' Dynamic Programming
Runtime: 145 ms, faster than 76.94% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
Memory Usage: 13.8 MB, less than 95.05% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0] * len(prices)
        
        for _ in range(k):
            pos = -prices[0]
            profit = 0
            
            for i in range(1, len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
                
        return dp[-1]


solution = Solution()
print(solution.maxProfit(2, [2,4,1])) # 2
print(solution.maxProfit(2, [3,2,6,5,0,3])) # 7
