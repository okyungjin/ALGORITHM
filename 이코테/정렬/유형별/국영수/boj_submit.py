# https://www.acmicpc.net/problem/14888

# Python 3
# 메모리: 86456 KB
# 시간: 440 ms

import sys

input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])