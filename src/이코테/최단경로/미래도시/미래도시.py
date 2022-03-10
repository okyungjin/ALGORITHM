# -*- coding: utf-8 -*-
import pprint as pp

# f = open('src/이코테/최단경로/미래도시.txt', 'r')
f = open('src/이코테/최단경로/미래도시2.txt', 'r')

INF = int(1e9)

n, m = map(int, f.readline().rstrip().split())

company = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    company[a][a] = 0

for _ in range(m):
    a, b = map(int, f.readline().rstrip().split())
    company[a][b] = 1
    company[b][a] = 1


x, k = map(int, f.readline().rstrip().split())

for r in range(1, n + 1):
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            company[p][q] = min(company[p][q], company[p][r] + company[r][q])


result = company[1][k] + company[k][x]

if result >= INF:
    print(-1)
else:
    print(result)


#pp.pprint(company)
'''
[[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
 [1000000000, 0, 1, 1, 1, 2],
 [1000000000, 1, 0, 2, 1, 2],
 [1000000000, 1, 2, 0, 1, 1],
 [1000000000, 1, 1, 1, 0, 1],
 [1000000000, 2, 2, 1, 1, 0]]
 '''