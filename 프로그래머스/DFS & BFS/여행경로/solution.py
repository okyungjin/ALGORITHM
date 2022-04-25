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