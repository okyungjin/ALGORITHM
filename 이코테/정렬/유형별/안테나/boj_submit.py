#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://www.acmicpc.net/problem/18310
# [1차] 시간 초과

import sys

input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

def get_distances(houses, idx):
    dist = houses[idx]
    result = 0
    for pos in houses:
        result += abs(dist - pos)
    return result


houses.sort()
min_val = 100000
min_idx = 0
idx = 0
while idx >= 0 and idx < len(houses):
    temp = get_distances(houses, idx)
    if temp < min_val:
        min_val = temp
        min_idx = idx
    idx += 1

print(houses[min_idx])