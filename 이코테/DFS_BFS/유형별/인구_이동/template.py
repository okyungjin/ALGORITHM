#-*-coding:utf-8-*-

# 난이도 2
# 풀이 시간 40분
# 시간 제한 2초

# BOJ:16234 인구 이동
# https://www.acmicpc.net/problem/16234

import os
import pprint as pp

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input2.txt'), 'r')

n, l, r = map(int, f.readline().split())
size = n + (n - 1)

def generate_new_map(n, size):
    maps = [[] * size for _ in range(size)]
    for i in range(size):
        if i % 2 == 0:
            row = list(map(int, f.readline().split()))
            new_row = []
            for j in range(n):
                new_row.append(row[j])
                if len(new_row) < size:
                    new_row.append('O') # 벽
            maps[i].append(new_row)
        else:
            maps[i].append(['O'] * size)
    return maps


dx = [0, 0, -2, 2]
dy = [2, -2, 0, 0]


maps = generate_new_map(n, size)
for i in range(size):
    for j in range(size):
        print(i, j)









