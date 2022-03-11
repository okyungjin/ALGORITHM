# 선택 정렬 (Selection Sort)

# 1. 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾼다
# 2. 그 다음 작은 데이터를 선택해 두 번째 데이터와 바꾼다
# 3. 이 과정을 반복한다

# 가장 작은 데이터를 '선택'하기 때문에 선택 정렬이라고 한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
		
	array[i], array[min_index] = array[min_index], array[i]

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]