# Meduim
# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List

'''
Runtime: 42 ms, faster than 98.26% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.2 MB, less than 9.51% of Python3 online submissions for Satisfiability of Equality Equations.
'''
ASCII_a = ord('a')
ASCII_z = ord('z')
SIZE = ASCII_z - ASCII_a + 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            # with path compress
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def convertCharToIndex(char: str) -> int:
            return ord(char) - ASCII_a


        parent = [i for i in range(SIZE)]
        for e in equations:
            c1, c2 = e[0], e[-1]
            isEqualOperator = e[1] == '='

            if isEqualOperator:
                idx1, idx2 = convertCharToIndex(c1), convertCharToIndex(c2)
                parent[find(idx1)] = find(idx2)

        for e in equations:
            c1, c2 = e[0], e[-1]
            isNotEqualOperator = e[1] == '!'
            idx1, idx2 = convertCharToIndex(c1), convertCharToIndex(c2)

            if isNotEqualOperator and find(idx1) == find(idx2):
                return False
                
        return True


solution = Solution()
print(solution.equationsPossible(["a==b","b!=a"])) # false
print(solution.equationsPossible(["b==a","a==b"])) # true
print(solution.equationsPossible(["a==b","b!=c","c==a"])) # false
