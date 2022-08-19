INF = 10e9
answer = INF

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    visited = [False] * n

    dfs(begin, target, words, n, visited, 0)

    return answer


def diff_one_char(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1


def dfs(start, target, words, n, visited, count):
    global answer

    if start == target:
        if answer > count:
            answer = count
        return
    
    for i in range(n):
        if diff_one_char(start, words[i]) and not visited[i]:
            visited[i] = True
            dfs(words[i], target, words, n, visited, count + 1)
            visited[i] = False # back-tracking



ans = solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
print(ans)