import heapq

answer = ['ICN']

def solution(tickets):
    routes = {}

    for ticket in tickets:
        start  = ticket[0]
        end = ticket[1]
        routes.setdefault(start, [])
        heapq.heappush(routes[start], end)

    go(len(tickets), routes, 'ICN', 0)
    return answer


def go(n, routes, start, used_tickets):
    if n == used_tickets:
        return

    if start not in routes.keys() or len(routes[start]) == 0:
        backstack = answer.pop()
        go(n, routes, backstack, used_tickets - 1)
        return
    
    nxt = heapq.heappop(routes[start])
    answer.append(nxt)
    go(n, routes, nxt, used_tickets + 1)

    
print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))

# Backtrack 로직 추가가 필요함 


"""Reference
# https://deok2kim.tistory.com/118

from collections import defaultdict, deque

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes:
        routes[key].sort(reverse=True) # pop()으로 알파벳 순서가 가장 빠른 것을 꺼내므로 reverse 활성화

    q = deque(['ICN'])
    while q:
        cur = q[-1]
        
        if not routes[cur]:
            answer.append(q.pop())
        else:
            q.append(routes[cur].pop())
    answer.reverse()
    return answer


# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
"""