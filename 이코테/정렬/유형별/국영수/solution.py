#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://www.acmicpc.net/problem/10825

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

n = int(f.readline())
students = []
for _ in range(n):
    students.append(f.readline().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])