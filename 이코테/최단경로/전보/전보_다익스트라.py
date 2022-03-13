# -*- coding: utf-8 -*-

# 본 문제의 조건을 살펴보면
# 1 <= n <= 30 000
# 1 <= m <= 200 000
# n, m 의 범위가 충분히 크기 때문에 우선순위 큐를 이용한 다익스트라 알고리즘을 작성해야 한다.
# 최단경로 유형 풀이 시에는 범위를 유심히 살펴보자!

import pprint as pp
import heapq

INF = int(1e9)

f = open('src/이코테/최단경로/전보/전보.txt', 'r')

# n: 도시의 개수
# m: 통로의 개수
# c: 메세지를 보내고자 하는 도시
n, m, start = map(int, f.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# 간선의 정보 받기
for _ in range(m):
  x, y, z = map(int, f.readline().rstrip().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, cur = heapq.heappop(q)
    if distance[cur] < dist:
        continue

    # 인접 노드 확인
    for i in graph[cur]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for dist in distance:
  if dist == INF: continue
  count += 1
  max_distance = max(max_distance, dist)

# 시작 노드 제외
print(count - 1, max_distance)

