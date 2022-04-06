# https://www.acmicpc.net/problem/14888

# PyPy3
# 메모리: 637644 KB
# 시간: 2584 ms

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # [+, -, *, /]

min_ans = int(1e9)
max_ans = -int(1e9)

def cal(oper_idx, result, next_num):
    if oper_idx == 0:
        return result + next_num
    if oper_idx == 1:
        return result - next_num
    if oper_idx == 2:
        return result * next_num
    if oper_idx == 3:
        num = result // next_num
        if num >= 0:
            return num
        return - 1 * (abs(result) // abs(next_num))

opers = []
for i in range(4):
    while operators[i] > 0:
        opers.append(i)
        operators[i] -= 1

for exp in list(permutations(opers, n - 1)):
    result = nums[0]
    for i in range(1, n):
        result = cal(exp[i-1], result, nums[i])

    min_ans = min(min_ans, result)
    max_ans = max(max_ans, result)

print(max_ans)
print(min_ans)