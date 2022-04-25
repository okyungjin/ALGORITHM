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