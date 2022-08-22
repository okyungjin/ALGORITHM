# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    '''bfs'''
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 유효하지 않은 좌표
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 처음 방문
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))


    answer = maps[n - 1][m - 1]
    return -1 if answer == 1 else answer
    

print(solution([
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]]
)) # 11

print(solution([
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,0],
    [0,0,0,0,1]]
)) # -1

print(solution([
    [1,0,1,1,1],
    [1,1,1,0,1]]
)) # -1