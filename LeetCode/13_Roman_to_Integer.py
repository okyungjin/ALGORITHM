# Easy
# https://leetcode.com/problems/roman-to-integer/

END_OF_STR = '_'

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000 }

        s = s + END_OF_STR
        i = 0
        res = 0
        while True:
            if s[i] == END_OF_STR: return res
            if s[i + 1] == END_OF_STR: return res + dict[s[i]]

            roman = s[i] + s[i + 1]
            if roman in dict:
                res += dict[roman]
                i += 2
            else:
                res += dict[roman[0]]
                i += 1
        
        return res



solution = Solution()
print(solution.romanToInt('III'))
print(solution.romanToInt('LVIII'))
print(solution.romanToInt('MCMXCIV'))
