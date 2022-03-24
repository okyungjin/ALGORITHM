#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

n = f.readline().rstrip()

arr = list(n)

left_sum = 0
for i in range(len(arr) / 2):
  left_sum += int(arr[i])

right_sum = 0
for i in range(len(arr) / 2, len(arr)):
  right_sum += int(arr[i])

if left_sum == right_sum:
  print('LUCKY')
else:
  print('READY')