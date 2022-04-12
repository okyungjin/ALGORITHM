#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# https://programmers.co.kr/learn/courses/30/lessons/42889

import heapq

def solution(N, stages):
    stages.sort()
    counts = [0 for _ in range(N + 2)]
    for stage in stages:
        counts[stage] += 1

    q = []
    users = counts[-1]
    for i in range(len(counts) - 2, 0, -1):
        if counts[i] == 0:
            heapq.heappush(q, (0, i))
        else:
            users += counts[i]
            failure = counts[i] * 1.0 / users
            heapq.heappush(q, (-failure, i))
    
    result = []
    while q:
        a = heapq.heappop(q)
        result.append(a[1])

    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
