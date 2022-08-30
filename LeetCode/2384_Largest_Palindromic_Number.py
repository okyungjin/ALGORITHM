class Solution:
    def largestPalindromic(self, num: str) -> str:
        copied_num = num
        if copied_num.strip('0') == '': return '0'

        counter = [0] * 10
        left_palindrome = [] # when "7449447", left_palindrome is [7, 4, 4]
        
        for n in num: counter[int(n)] += 1
            
        max_odd_num = -1

        for i in range(9, -1, -1):
            n, count = i, counter[i]
            if count == 0: continue

            if count % 2 != 0: # 홀수
                count -= 1

                if max_odd_num == -1:
                    max_odd_num = n

            while count > 0:
                left_palindrome.append(str(n))
                count -= 2

        mid_palindrome = '' if max_odd_num == -1 else str(max_odd_num)
        answer = ''.join(left_palindrome) + mid_palindrome + ''.join(left_palindrome[::-1])

        return answer.strip('0')


# TEST
solution = Solution()

print(solution.largestPalindromic('444947137')) # '7449447'
print(solution.largestPalindromic('00009')) # '9'
print(solution.largestPalindromic('00001105')) # '1005001'
print(solution.largestPalindromic('0000')) # '0'
print(solution.largestPalindromic('5736732')) # '73637'