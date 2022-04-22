import heapq

answer = ['ICN']

def solution(tickets):
    routes = {}

    for ticket in tickets:
        start  = ticket[0]
        end = ticket[1]
        routes.setdefault(start, [])
        heapq.heappush(routes[start], end)

    go(len(tickets), routes, 'ICN')
    return answer


def go(n, routes, start):
    if n + 1 == len(answer):
        return
    
    nxt = heapq.heappop(routes[start])
    answer.append(nxt)
    go(n, routes, nxt)

    
# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))