# Meduim
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

'''
Runtime: 3045 ms, faster than 40.16% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.8 MB, less than 80.31% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        answer = bitLen = 1

        for i in range(2, n + 1):
            if self.isPowerOfTwo(i): bitLen += 1
            # answer = (answer << bitLen) + i
            answer = (answer << bitLen) + i
            answer %= MOD
            
        return answer

    def isPowerOfTwo(self, num: int):
        return num & (num - 1) == 0


solution = Solution()
print(solution.concatenatedBinary(1)) # 1
print(solution.concatenatedBinary(3)) # 27
print(solution.concatenatedBinary(12)) # 505379714
