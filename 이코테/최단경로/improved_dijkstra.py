# 개선된 다익스트라
import heapq

INF = int(1e9)

f = open('src/이코테/최단경로/dijkstra.txt', 'r')

node_cnt, edge_cnt = map(int, f.readline().rstrip().split())
start = int(f.readline().rstrip())

graph = [[] for _ in range(node_cnt + 1)]
distance = [INF] * (node_cnt + 1)

for _ in range(edge_cnt):
	start_node, end_node, cost = map(int, f.readline().rstrip().split())
	graph[start_node].append((end_node, cost))


def improved_dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue

		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))



improved_dijkstra(start)

for i in range(1, node_cnt + 1):
	if (distance[i] == INF):
		print('Infinity')
	else:
		print(distance[i])