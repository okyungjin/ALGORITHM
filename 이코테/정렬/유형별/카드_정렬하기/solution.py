#-*-coding:utf-8-*-

# 난이도 2
# 풀이 시간 30분
# 시간 제한 2초

# https://www.acmicpc.net/problem/1715

# import sys
# input = sys.stdin.readline

# import os
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# f = open(os.path.join(__location__, 'input.txt'), 'r')
# input = f.readline

import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) != 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    sum_val = first + second
    result += sum_val
    heapq.heappush(q, sum_val)
print(result)