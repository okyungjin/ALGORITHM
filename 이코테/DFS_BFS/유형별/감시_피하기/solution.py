#-*-coding:utf-8-*-

# 난이도 2.5
# 풀이 시간 6분
# 시간 제한 2초

# https://www.acmicpc.net/problem/18428

import os
import pprint as pp
from itertools import combinations
import copy



global f
def INPUT():
    SUBMIT_BOJ = False
    if SUBMIT_BOJ:
        return input()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, 'input1.txt'), 'r')
    return f.readline()


n = int(INPUT())
maps = [INPUT().split() for _ in range(n)]
print(maps)

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
            if maps[i][j] == 'T':
                result.append((i, j))
    return result


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 선생님이 감시
def watch(maps):
    for t in teachers:
        for i in range(4):
            nx = t[0]
            ny = t[1]
            while (nx >= 0 and nx < len(maps) and ny >=0 and ny < len(maps)):
                if maps[nx][ny] == 'O':
                    break
                if maps[nx][ny] == 'S':
                    return False
                nx += dx[i]
                ny += dy[i]
    return True

    
# 장애물 설치하기
flag = False
teachers = get_teachers(maps)
for combi in get_combinations(maps):
    temp = copy.deepcopy(maps)
    for pos in combi:
        temp[pos[0]][pos[1]] = 'O'
    if watch(temp):
        flag = True
        print('YES')
        break

if not flag:
    print('NO')