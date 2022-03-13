from collections import deque

# n, m = 5, 6
#
# maps = [
#     [1,0,1,0,1,0],
#     [1,1,1,1,1,1],
#     [0,0,0,0,0,1],
#     [1,1,1,1,1,1],
#     [1,1,1,1,1,1],
# ]

n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()

    # 첫 번째 노드 삽입
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표 초과
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물을 만날 경우
            if maps[x][y] == 0:
                continue

            # 노드를 처음 방문
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 가장 마지막 노드 출력
    return maps[n-1][m-1]


result = bfs(0, 0)
print(result)