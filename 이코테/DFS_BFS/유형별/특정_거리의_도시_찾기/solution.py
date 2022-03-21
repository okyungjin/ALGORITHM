import os
from collections import deque


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

nTestCase = int(f.readline())

# N M K X
# A B (from, to)

for _ in range(nTestCase):
    nCity, nEdge, k, start = map(int, f.readline().split())
    graph = [[] for _ in range(nCity + 1)]

    # init graph
    for _ in range(nEdge):
        st, end = map(int, f.readline().split())
        graph[st].append(end)

    distance = [-1] * (nCity + 1)

    distance[start] = 0

    q = deque([start])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    check = False
    for i in range(1, nCity + 1):
        if distance[i] == k:
            print(i)
            check = True

    if check == False:
        print(-1)

    print('*----------*')