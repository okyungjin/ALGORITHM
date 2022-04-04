# PyPy3 정답
#   메모리: 14208 KB
#   시간: 1360 ms
# Python3 80%에서 시간 초과

import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def process(x, y, index):
    # (x, y)와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))

    union[x][y] = index # 현재 연합의 번호 할당
    population = graph[x][y] # 현재 연합의 전체 인구 수
    n_country = 1 # 현재 연합의 국가 수

    # BFS
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 넘어감 or 이미 연합
            if nx < 0 or nx >= n or ny < 0 or ny >= n or union[nx][ny] != -1:
                continue

            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                q.append((nx, ny))
                union[nx][ny] = index
                population += graph[nx][ny]
                n_country += 1
                united.append((nx, ny))

    for i, j in united:
        graph[i][j] = population // n_country
    return n_country
            
total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 아직 처리 전이라면
                process(i, j, index)
                index += 1
    if index == n * n:
        break;
    total_count += 1

print(total_count)