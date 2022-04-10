#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://www.acmicpc.net/problem/18310

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

n = int(f.readline())
houses = list(map(int, f.readline().split()))

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