#-*-coding:utf-8-*-

# 난이도 2
# 풀이 시간 30분
# 시간 제한 2초

# [BOJ] 삼성전자 SW 역량 테스트
# https://www.acmicpc.net/problem/14888

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

n = int(f.readline())
nums = list(map(int, f.readline().split()))
operators = list(map(int, f.readline().split())) # [+, -, *, /]

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
        num = result * next_num
        if num >= 0:
            return num
        return - 1 * (abs(result) // abs(next_num))


def dfs(result, num_index):
    if num_index == n - 1:
        min_ans = min(min_ans, result)
        max_ans = max(max_ans, result)
        return result
    
    # for i in range(4):
    #     if operators[i] != 0:
    #         operators[i] -= 1
    #         dfs(i, cal(i, result, nums[num_index + 1]), num_index + 1)
    #         operators[i] += 1
            
answer = dfs(nums[0], 0)
print(min_ans)
print(max_ans)