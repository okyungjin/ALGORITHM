# Meduim
# https://leetcode.com/problems/utf-8-validation/

from typing import List
from re import compile

'''
Runtime: 227 ms, faster than 29.97% of Python3 online submissions for UTF-8 Validation.
Memory Usage: 14.9 MB, less than 15.94% of Python3 online submissions for UTF-8 Validation.
'''
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        stringifiedBytes = [bin(byte)[2:].zfill(8) for byte in data]
        byteSize = len(data)
        idx = 0

        bytePatterns = [compile('0[0-1]{7}'), compile('110[0-1]{4}'), compile('1110[0-1]{3}'), compile('11110[0-1]{2}')]
        followingBytePattern = compile('10[0-1]{6}')

        while idx < byteSize:
            matched = False
            for patternNo, pattern in enumerate(bytePatterns):
                if pattern.match(stringifiedBytes[idx]) is None: continue

                if patternNo == 0:
                    matched = True
                    break

                if idx + patternNo >= byteSize: return False

                for j in range(1, patternNo + 1):
                    nextByte = stringifiedBytes[idx + j]
                    if followingBytePattern.match(nextByte) is None:
                        return False

                matched = True
                idx += patternNo

            if not matched: return False
            idx += 1

        return True


solution = Solution()
print(solution.validUtf8([197,130,1])) # True
print(solution.validUtf8([235,140,4])) # False
print(solution.validUtf8([240,162,138,147])) # True
print(solution.validUtf8([39,89,227,83,132,95,10,0])) # False
print(solution.validUtf8([10])) # True
