# Level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=python3

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX_SIZE = 101
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    maps = generate2dSquare(MAX_SIZE, -1)

    for lbx, lby, rtx, rty in rectangle:
        lbx, lby, rtx, rty = lbx * 2, lby * 2, rtx * 2, rty * 2

        for x in range(lbx, rtx + 1):
            for y in range(lby, rty + 1):
                if maps[x][y] == 0:
                    continue

                if x == lbx or x == rtx or y == lby or y == rty:
                    maps[x][y] = 1
                else:
                    maps[x][y] = 0

    startX, startY = characterX * 2, characterY * 2
    endX, endY = itemX * 2, itemY * 2

    '''bfs'''
    queue = deque([(startX, startY)])
    while queue:
        x, y = queue.popleft()
        

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= MAX_SIZE or ny < 0 or ny >= MAX_SIZE:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[endX][endY] // 2


def generate2dSquare(size, initial_value = 0):
    return [[initial_value] * size for i in range(size)]


def print2dGraph(graph, limit = None):
    for i in range(limit + 1):
        print('[%2d]'%i, end = ' ')
        for j in range(limit + 1):
            print('%2s'%graph[i][j], end = ' ')
        print()

    sliced_rows = graph if limit is None else graph[:limit + 1]
    for row in sliced_rows:
        sliced_cols = row if limit is None else row[:limit + 1]
        



print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
print(solution([[1,1,5,7]], 1, 1, 4, 7)) # 9
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)) # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)) # 10
