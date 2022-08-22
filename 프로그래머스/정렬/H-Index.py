# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    citations.sort(reverse=True)
    for idx, citn in enumerate(citations):
        if idx >= citn: return idx

    return len(citations)


print(solution([3, 0, 6, 1, 5]))
