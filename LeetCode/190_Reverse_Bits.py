# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        MAX_SIZE = 32
        result = 0

        for i in range(MAX_SIZE):
            last_bit = (n >> i) & 1
            if last_bit:
                result += 1 << (31 - i)

        return result
        

# TEST
solution = Solution()

print(solution.reverseBits(964176192))
print(solution.reverseBits(4294967293))