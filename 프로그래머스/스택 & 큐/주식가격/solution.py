from collections import deque

def solution(prices):
    answer = []

    q = deque(prices)

    while q:
        cur = q.popleft()
        answer.append(count(cur, q))

    return answer

def count(price, queue):
    result = 0
    for q in queue:
        if q >= price:
            result += 1
    return result


print(solution([1, 2, 3, 2, 3]))


# [정확성 테스트] 테스트 1 제외 오답
# [효율성 테스트] 오답 ..