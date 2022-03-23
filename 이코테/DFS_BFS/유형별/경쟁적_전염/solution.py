# 경쟁적 전염

# N 시험관 크기 (1, 200)
# K 바이러스 종류 (1, 1000)

# 바이러스는 1초마다 상하좌우로 증식
# 매초 번호가 낮은 종류의 바이러스부터 증식

# 증식 조건
# 이미 바이러스가 있다면 다른 바이러스가 들어갈 수 없음

# 출력
# S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류
    # 시작점 (1, 1)
# 존재하지 않으면 0


from cmath import inf
import heapq
import os
import pprint as pp

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

n, k = map(int, f.readline().split())

data = [[] for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, f.readline().split()))
s, x, y = map(int, f.readline().split())


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def infect(x, y, virus_kind):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < n and data[nx][ny] == 0:
            data[nx][ny] = virus_kind

time = 0
q = []
for i in range(n):
    for j in range(n):        
        if data[i][j] > 0:
            heapq.heappush(q, (data[i][j], (i, j)))


while q:
    if k == time:
        break
    virus = heapq.heappop(q)
    time += 1
    infect(virus[1][0], virus[1][1], virus[0])


answer = int(f.readline())
result = data[x-1][y-1]
print('정답' if result == answer else '오답', end = ': ')
print(result)