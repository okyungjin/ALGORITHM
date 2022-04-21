def solution(begin, target, words):
    # if target not in words:
    #     return 0

    visited = [False] * len(words)

    dfs(begin, target, words, 0)
    return -1


def dfs(begin, words, visited, count):
    for i in range(len(words)):
        if visited[i] or get_diff_count(begin, words[i]) > 1:
            continue


def get_diff_count(word1, word2):
    diff_count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1

    return diff_count


if __name__ == '__main__':
    _begin = 'hit'
    _target = 'cog'
    _words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    
    ans = solution(_begin, _target, _words)
    print(ans)
