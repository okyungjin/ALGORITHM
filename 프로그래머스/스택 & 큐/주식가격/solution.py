from collections import deque

def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        cur = q.popleft()
        answer.append(count_time(cur, q))

    return answer


def count_time(price, queue):
    time = 0
    for q in queue:
        time += 1
        if price > q:
            break
    return time


print(solution([1, 2, 3, 2, 3]))