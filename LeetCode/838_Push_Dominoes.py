import re

''' RegExp
Runtime: 675 ms, faster than 39.26% of Python3 online submissions for Push Dominoes.
Memory Usage: 18.1 MB, less than 54.67% of Python3 online submissions for Push Dominoes. 
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:        
        d = dominoes

        p1 = re.compile('R[\.]{2,}L') # R.L pattern
        p2 = re.compile('[\.]+L') # .L pattern
        p3 = re.compile('R[\.]+')
        
        for matched in p1.finditer(dominoes):
            left, right = matched.span()
            diff = right - left
            tmp = 'R' * (diff // 2)

            if diff % 2 != 0:
                tmp += '.'

            tmp += 'L' * (diff // 2)

            if left == 0:
                d = tmp + d[right:]
            else:
                d = d[:left] + tmp + d[right:]

        for matched in p2.finditer(d):
            left, right = matched.span()

            if left > 0 and d[left - 1] == 'R':
                continue

            diff = right - left
            tmp = 'L' * diff

            if left == 0:
                d = tmp + d[right:]
            else:
                d = d[:left] + tmp + d[right:]
        
        for matched in p3.finditer(d):
            left, right = matched.span()

            if right < len(d) and d[right] == 'L':
                continue


            diff = right - left
            tmp = 'R' * diff

            if left == 0:
                d = tmp + d[right:]
            else:
                d = d[:left] + tmp + d[right:]

        return d

        
solution = Solution()
a1 = solution.pushDominoes('.L.R...LR..L..')
print(a1, a1 == 'LL.RR.LLRRLL..')

a2 = solution.pushDominoes('RR.L')
print(a2, a2 == 'RR.L')