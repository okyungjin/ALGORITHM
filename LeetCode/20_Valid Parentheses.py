# Easy
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {'}':'{', ')':'(', ']':'['}

        for bracket in s:
            if bracket in bracket_pair.values():
                stack.append(bracket)
            else:
                if stack and bracket_pair[bracket] == stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack: return False
        return True


solution = Solution()
print(solution.isValid('()'))
# print(solution.isValid('()[]{}'))