# Easy
# https://leetcode.com/problems/hamming-distance/

'''
Runtime: 51 ms, faster than 44.38% of Python3 online submissions for Hamming Distance.
Memory Usage: 13.9 MB, less than 63.15% of Python3 online submissions for Hamming Distance.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


print(Solution().hammingDistance(1, 4)) # 2
print(Solution().hammingDistance(3, 1)) # 1
