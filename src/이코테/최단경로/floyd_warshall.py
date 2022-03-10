from random import randrange


INF = int(1e9)

f = open('src/이코테/최단경로/floyd_warshall.txt', 'r')

node_cnt = int(f.readline().rstrip())
edge_cnt = int(f.readline().rstrip())

graph = [[INF] * (node_cnt + 1) for _ in range(node_cnt + 1)]


for a in range(1, node_cnt + 1):
	for b in range(1, node_cnt + 1):
		if a == b:
			graph[a][b] = 0


for _ in range(edge_cnt):
	a, b, c = map(int, f.readline().rstrip().split())
	graph[a][b] = c


for k in range(1, node_cnt + 1):
	for a in range(1, node_cnt + 1):
		for b in range(1, node_cnt + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, node_cnt + 1):
	for b in range(1, node_cnt + 1):
		if graph[a][b] == INF:
			print('Infinity', end=' ')
		else:
			print(graph[a][b], end=' ')
	print()