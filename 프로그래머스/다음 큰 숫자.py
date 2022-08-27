# Level 2
# ool.programmers.co.kr/learn/courses/30/lessons/12911

from collections import Counter

MAX_NUM = 1_000_001
def solution(n):
    for num in range(n, MAX_NUM):
        if num > n and bin(n).count('1') == bin(num).count('1'):
            return num

    return n

print(solution(78))
print(solution(15))
