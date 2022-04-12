#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 30분
# 시간 제한 1초

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')
input = f.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

counts = [0 for _ in range(data[-1] + 1)]

for num in data:
    counts[num] += 1

res = 0
for i in range(len(counts) - 1, 0, -1):
    if counts[i] >= i:
        res = i
        break

print(res)



