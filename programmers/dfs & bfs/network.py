def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, n, computers)
            answer += 1

    return answer


def dfs(start, visited, n, computers):
    visited[start] = True

    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i, visited, n, computers)


if __name__ == '__main__':
    _n = 3
    _computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    # _computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    ans = solution(_n, _computers)
    print(ans)
