visited = []

def solution(n, computers):
    global visited

    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, n, computers)
            answer += 1

    return answer


def dfs(start, n, computers):
    visited[start] = True
    
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            dfs(i, n, computers)


res = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(res)