# Meduim
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0: res += diff

        if res < 0: return 0
        return res
    