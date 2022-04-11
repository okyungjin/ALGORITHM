#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://www.acmicpc.net/problem/18310
# [1차] 시간 초과
# [2차] 정답

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])