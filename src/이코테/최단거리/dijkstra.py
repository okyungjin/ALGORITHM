# 간단한 다익스트라
INF = int(1e9)

f = open('src/이코테/최단거리/dijkstra.txt', 'r')

node_cnt, edge_cnt = map(int, f.readline().rstrip().split())
start = int(f.readline().rstrip())

graph = [[] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt + 1)
dist = [INF] * (node_cnt + 1)

for _ in range(edge_cnt):
	start_node, end_node, cost = map(int, f.readline().rstrip().split())
	graph[start_node].append((end_node, cost))


def get_shortest_node():
	min_val = INF
	result = 0
	for i in range(1, node_cnt + 1):
		if dist[i] < min_val and not visited[i]:
			min_val = dist[i]
			result = i
	return result


def dijkstra(start):
	dist[start] = 0
	visited[start] = True

	for linked in graph[start]:
		dist[linked[0]] = linked[1] # linked: (end, dist)

	for _ in range(node_cnt - 1):
		now = get_shortest_node()
		visited[now] = True
		
		for i in graph[now]:
			cost = dist[now] + i[1]
			if cost < dist[i[0]]:
				dist[i[0]] = cost


dijkstra(start)

for i in range(1, node_cnt + 1):
	if (dist[i] == INF):
		print('Infinity')
	else:
		print(dist[i])