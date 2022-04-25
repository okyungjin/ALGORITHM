import math
from collections import deque

MAX_PROGRESS = 100

def solution(progresses, speeds):
    answer = [1]

    q = deque([])

    for i in range(len(progresses)):
        jobs = math.ceil((MAX_PROGRESS - progresses[i]) / speeds[i])
        q.append(jobs)
    
    before_job = q.popleft()
    while q:
        cur = q.popleft()
        if before_job >= cur:
            answer[-1] += 1
        else:
            answer.append(1)
            before_job = cur
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))