#-*-coding:utf-8-*-

# A16. 연구소

# 벽을 3개 설치하는 모든 경우의 수를 게산해야 한다.
# 경우의 수는 64C3이므로 100,000 보다도 작은 수이다.
# 모든 경우의 수를 고려하여도 제한 시간(2초) 안에 해결할 수 있다.

# 모든 조합을 계산할 때는
# 1. 파이썬의 조합 라이브러리를 이용하거나
# 2. DFS / BFS를 이용하여 해결할 수 있다.

# 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에, 조합 마다의 안전 영역 크기를 계산한다.
# 안전 영역 크기를 구하는 것 또한 DFS나 BFS를 이용하여 계산할 수 있다.

import os
from enum import Enum
import pprint as pp

class Area(Enum):
	EMPTY = 0
	WALL = 1
	VIRUS = 2


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input1.txt'), 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
graph = []
temp = []

n, m = map(int, f.readline().split())


for _ in range(n):
	graph.append(list(map(lambda x: Area(int(x)) , f.readline().split())))
	temp.append([Area.EMPTY] * m)


def virus(x, y):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if (nx >= 0 and nx < n and ny >= 0 and ny < m) and temp[nx][ny] == Area.EMPTY:
			temp[nx][ny] = Area.VIRUS
			virus(nx, ny)
		

# 현재 그래프에서 안전 영역의 크기를 계산하는 함수
def get_size_of_safe_area():
	size = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == Area.EMPTY:
				size += 1
	return size



# DFS를 이용해 울타리를 설치하면서 매번 안전 영역의 크기를 계산하는 함수
def dfs(fense_cnt):
	global result

	# 울타리가 3개 설치된 경우
	if fense_cnt == 3:
		for i in range(n):
			for j in range(m):
				temp[i][j] = graph[i][j]
		
		# 각 바이러스의 위치에서 전파 진행
		for i in range(n):
			for j in range(m):
				if temp[i][j] == Area.VIRUS:
					virus(i, j)
		
		# 안전 영역의 최댓값 계산
		result = max(result, get_size_of_safe_area())
		return
		
	# 빈 공간에 울타리 설치
	for i in range(n):
		for j in range(m):
			if graph[i][j] == Area.EMPTY:
				graph[i][j] = Area.WALL
				fense_cnt += 1
				dfs(fense_cnt)
				graph[i][j] = Area.EMPTY
				fense_cnt -= 1


dfs(0)

answer = int(f.readline())
print('정답' if result == answer else '오답', end = ': ')
print(result)