n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# n, m = 4, 5

# graph = [
#   [0, 0, 1, 1, 0],
#   [0, 0, 0, 1, 1],
#   [1, 1, 1, 1, 1],
#   [0, 0, 0, 0, 0],
# ]

def dfs(x, y):
  # 좌표를 넘어갈 경우
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  # 칸막이일 경우
  if graph[x][y] == 1:
    return False

  # 방문 처리
  graph[x][y] = 1
  dfs(x - 1, 0)
  dfs(x + 1, 0)
  dfs(x, y - 1)
  dfs(x, y + 1)
  return True
  

count = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j):
      count += 1

print(count)