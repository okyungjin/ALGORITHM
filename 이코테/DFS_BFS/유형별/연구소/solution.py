#-*-coding:utf-8-*-

# A16. 연구소

# 벽을 3개 설치하는 모든 경우의 수를 게산해야 한다.
# 경우의 수는 64C3이므로 100,000 보다도 작은 수이다.
# 모든 경우의 수를 고려하여도 제한 시간(2초) 안에 해결할 수 있다.

# 모든 조합을 계산할 때는
# 1. 파이썬의 조합 라이브러리를 이용하거나
# 2. DFS / BFS를 이용하여 해결할 수 있다.

# 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에, 조합 마다의 안전 영역 크기를 계산한다.
# 안전 영역 크기를 구하는 것 또한 DFS나 BFS를 이용하여 게산할 수 있다.

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
graph = []
temp = []

n, m = map(int, f.readline().split())

for _ in range(n):
	graph.append(list(map(int, f.readline().split())))
	temp.append([0] * m)

	
def virus(x, y):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if nx >= 0 and nx < n and ny >= 0 and ny < m:
			if temp[nx][ny] == 0:
				temp[nx][ny] = 2
				virus(nx, ny)
		

# 현재 그래프에서 안전 영역의 크기를 계산하는 함수
def get_score():
	size = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 0:
				size += 1
	return size



# DFS를 이용해 울타리를 설치하면서 매번 안전 영역의 크기를 계산하는 함수
def dfs(count):
	global result

	# 울타리가 3개 설치된 경우
	if count == 3:
		for i in range(n):
			for j in range(m):
				temp[i][j] = graph[i][j]
		
		# 각 바이러스의 위치에서 전파 진행
		for i in range(n):
			for j in range(m):
				if temp[i][j] == 2:
					virus(i, j)
		
		# 안전 영역의 최댓값 계산
		result = max(result, get_score())
		return
		
	# 빈 공간에 울타리 설치
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 0:
				graph[i][j] = 1
				count += 1
				dfs(count)
				graph[i][j] = 0
				count -= 1


dfs(0)

answer = int(f.readline())
if result == answer:
	print('정답: {:d}'.format(result))
else:
	print('오답: {:d}'.format(result))