#-*-coding:utf-8-*-

# 난이도 2.5
# 풀이 시간 6분
# 시간 제한 2초

import os
import pprint as pp
from itertools import combinations
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

n = int(f.readline())
maps = [f.readline().split() for _ in range(n)]

# 장애물 설치 조합 찾기
def get_combinations(maps):
    empty = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 'X':
                empty.append((i, j))
    return list(combinations(empty, 3))


# 선생님 위치 찾기
def get_teachers(maps):
    result = []
    # 선생님 위치 찾기
    for i in range(n):
        for j in range(n):
            result.append(maps[i][j])
    return resulst


# 선생님이 감시
# TODO: FIXME
def watch(maps):
    return True

    
# 장애물 설치하기
flag = False
for combi in get_combinations(maps):
    temp = copy.deepcopy(maps)
    for pos in combi:
        temp[pos[0]][pos[1]] = 'O'
    if watch(temp):
        print('YES')
        flag = True
        break

if not flag:
    print('NO')



    


