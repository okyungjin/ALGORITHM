#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

data = f.readline().rstrip()

capitals = []
num_sum = 0
for char in data:
  if char.isupper():
    capitals.append(char)
  else:
    num_sum = int(char)

  capitals.sort()
  
  capitals.


  print()
  print()
  # 

answer = f.readline().rstrip()

print(data)
print('정답' if data == answer else '오답')