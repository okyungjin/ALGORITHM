# -*- coding: utf-8 -*-
import pprint as pp

INF = int(1e9)

f = open('src/이코테/최단경로/전보/전보.txt', 'r')

# n: 도시의 개수
# m: 통로의 개수
# c: 메세지를 보내고자 하는 도시
n, m, c = map(int, f.readline().rstrip().split())


graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0


for _ in range(m):
    x, y, z = map(int, f.readline().rstrip().split())
    graph[x][y] = z


totalTime = 0
nCanVisitCity = 0

for time in graph[c]:
    if time >= INF:
        continue

    if time != 0:
        nCanVisitCity += 1

    totalTime += time
    
    
print(nCanVisitCity, totalTime)


#pp.pprint(graph)


