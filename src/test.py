_graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]


def dfs(_graph, v,  visited):
    visited[v] = True  # 방문 처리
    print(v, end=' ')
    for neighbor in _graph[v]:
        if not visited[neighbor]:
            dfs(_graph, neighbor, visited)


visited = [False] * 9

dfs(_graph, 1, visited)
