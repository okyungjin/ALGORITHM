# Meduim
# https://leetcode.com/problems/bag-of-tokens/

from typing import List

'''
Runtime: 105 ms, faster than 25.94% of Python3 online submissions for Bag of Tokens.
Memory Usage: 14 MB, less than 39.62% of Python3 online submissions for Bag of Tokens.
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        usedTokens = score = left = 0
        right = len(tokens) - 1
 
        while usedTokens < len(tokens):
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            else:
                if score < 1 or usedTokens >= len(tokens) - 1: break
                power += tokens[right]
                score -= 1
                right -= 1
            usedTokens += 1            

        return score


solution = Solution()
print(solution.bagOfTokensScore([100], 50)) # 0
print(solution.bagOfTokensScore([100,200], 150)) # 1
print(solution.bagOfTokensScore([100,200,300,400], 200)) # 2
