#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://www.acmicpc.net/problem/18310

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

n = int(f.readline())
data = list(map(int, f.readline().split()))
data.sort()

print(data[(n - 1) // 2])