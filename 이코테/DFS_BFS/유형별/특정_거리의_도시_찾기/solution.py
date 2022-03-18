import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

# 특정 도시 X로 출발 -> 다익스트라
# 최단 거리가 K인 모든 도시의 번호 출력




# N M K X
# A B (from, to)

# bfs로 풀이
nCity, nEdge, start, k = map(int, f.readline().split())
graph = [[] for _ in range(nCity + 1)]

# init graph
for _ in range(nEdge):
    st, end = map(int, f.readline().split())
    graph[st].append((1, end))

print(graph)


# def dijsktra(graph, start, k):





