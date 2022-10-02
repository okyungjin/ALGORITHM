# Medium
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

''' Dynamic Programming
Runtime: 1602 ms, faster than 16.30% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 19.8 MB, less than 26.91% of Python3 online submissions for Number of Dice Rolls With Target Sum.
'''
class Solution:
    def numRollsToTarget(self, numOfDice: int, faces: int, target: int) -> int:
        MODOULO = 10 ** 9 + 7
        dp = {}

        def recursive(numOfDice, target):
            if numOfDice == 0:
                return target <= 0

            if (numOfDice, target) in dp:
                return dp[(numOfDice, target)]

            ways = 0
            
            for k in range(max(0, target - faces), target):
                ways += recursive(numOfDice - 1, k)

            dp[(numOfDice, target)] = ways

            return ways

        return recursive(numOfDice, target) % MODOULO