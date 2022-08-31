# Easy
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {')':'(', '}':'{', ']':'['}

        for bracket in s:
            if bracket in bracket_pair.values():
                stack.append(bracket)
                continue

            if stack and bracket_pair[bracket] == stack[-1]:
                stack.pop()
            else:
                return False 
            
        return False if stack else True


solution = Solution()
print(solution.isValid('()')) # True
print(solution.isValid('()[]{}')) # True
print(solution.isValid('(]')) # False