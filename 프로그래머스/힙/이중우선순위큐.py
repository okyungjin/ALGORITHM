import heapq
from collections import deque

def solution(operations):
    opers = deque(operations)

    min_heap = []
    max_heap = []

    while opers:
        oper, num = opers.popleft().split()
        num = int(num)
        if oper == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if not min_heap: continue
            if num == 1:
                popped = heapq.heappop(max_heap)
                min_heap.remove(-popped)
            elif num == -1:
                popped = heapq.heappop(min_heap)
                max_heap.remove(-popped)

    if not min_heap:
        return [0, 0]

    min_val = heapq.heappop(min_heap)
    max_val = -heapq.heappop(max_heap)
    return [max_val, min_val]


# print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))