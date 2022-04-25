from collections import deque
import heapq

def solution(priorities, location):
    target = (priorities[location], location)

    q = deque([])
    printer = []

    for i in range(len(priorities)):
        q.append((priorities[i], i))

    while q:
        cur = q.popleft()
        if move_to_back(cur, q):
            q.append(cur)
        else:
            printer.append(cur)
    
    answer = -1
    for i in range(len(printer)):
        if printer[i] == target:
            answer = i
            break

    return answer + 1
        

def move_to_back(cur, q):
    for priority in q:
        if priority[0] > cur[0]:
            return True
    return False


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
