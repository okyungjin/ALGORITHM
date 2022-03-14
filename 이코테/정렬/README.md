# 선택 정렬 (Selection Sort)

매번 가장 작은 데이터를 **선택**한다는 의미에서 **선택 정렬**이라고 한다.

## 과정
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾼다
- 그 다음 작은 데이터를 선택해 두 번째 데이터와 바꾼다
- 이 과정을 반복한다

```py
[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
[0, 5, 9, 7, 3, 1, 6, 2, 4, 8] # 가장 작은 0을 선택해 arr[0]과 swap한다.
[0, 1, 9, 7, 3, 5, 6, 2, 4, 8] # 그 다음 작은 1을 선택해 arr[1]과 swap한다.
[0, 1, 2, 7, 3, 5, 6, 9, 4, 8] # 이후 설명 생략
[0, 1, 2, 3, 7, 5, 6, 9, 4, 8]
[0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 시간 복잡도
  - $ O(N^2) $

## 구현 소스
```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
		
	array[i], array[min_index] = array[min_index], array[i]

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

----

# 삽입 정렬 (Insertion Sort)
데이터를 하나씩 확인하면서 각 데이터를 적절한 위치에 **삽입**한다.
> 삽입 정렬은 필요할 때만 위치를 바꾸므로 **데이터가 거의 정렬되어 있을 때** 훨씬 효율적이다.
## 과정
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
- 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에 그 위치에 삽입된다.
  
```py
    _
[7, 5, 9, 0, 3, 1, 6, 2, 4, 8] # 5를 꺼내 7 앞에 삽입한다.
       _
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8] # 9는 제자리에 둔다.
          _
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8] # 0을 꺼내 맨 앞에 삽입한다.
             _
[0, 5, 7, 9, 3, 1, 6, 2, 4, 8] # 3은 한 칸씩 왼쪽으로 이동하다가 자신보다 작은 0을 만났을 때 그 위치에 삽입된다.
                _                
[0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
                   _ 
[0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
                      _
[0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
                         _
[0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
                            _
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 시간 복잡도
최선의 경우 $O(N)$의 복잡도를 가진다.

## 구현 소스
```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1): # i부터 1까지 -1씩 감소
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j]
		else:
			break
		
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> 삽입 정렬은 **현재 리스트가 거의 정렬**되어 있을 때 매우 빠르게 동작한다.

----

<br/>

# 퀵 정렬 (Quick Sort)
퀵 정렬은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이며, 사용 빈도가 높다.

퀵 정렬은 **기준 데이터를 설정**하고, 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는** 로직으로 동작한다.

## 과정
1. `리스트의 첫 번째 데이터를` 피벗(Pivot)으로 설정한다.
     - **피벗**이란 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 **기준**을 말한다.
     - 피벗을 정하는 기준에 따라 퀵 정렬의 방식이 구분되는데, 해당 문서에서는 `리스트의 첫 번째 데이터를` **호어 분할 방식**(Hoare Partition)을 사용한다.
2. 왼쪽에서 피벗보다 큰 데이터를 찾고, 오른쪽에서는 피벗보다 작은 데이터를 찾는다.
3. 큰 데이터와 작은 데이터의 위치를 교환한다.
4. 5과정 전까지 `2`, `3` 과정을 반복한다.
5. 큰 데이터와 작은 데이터의 값이 엇갈릴 때, **작은 데이터와 피벗의 위치를 변경**한다.
6. 피벗을 기준으로 divide 한다.
7. 위의 과정을 반복한다.

```py
#1: pivot 설정

pivot
 _               
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


#2: 왼쪽 -> pivot보다 큰 데이터
# 오른쪽 -> pivot보다 작은 데이터
pivot보다 큼           pivot보다 작음
    _                    _
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


#3: swap
    _                    _
[5, 4, 9, 0, 3, 1, 6, 2, 7, 8]


#4: 반복
[5, 4, 2, 0, 3, 1, 6, 9, 7, 8]


#5: 값이 엇갈릴 때 '작은 데이터'와 피벗의 위치 변경
                _  _
[5, 4, 2, 0, 3, 1, 6, 9, 7, 8] 값이 엇갈림

 _              _
[1, 4, 2, 0, 3, 5, 6, 9, 7, 8] 작은 데이터와 pivot 위치 변경


#6: pivot을 기준으로 divide
[1, 4, 2, 0, 3] 5 [6, 9, 7, 8]


#7: divided에서 위의 과정을 반복한다.
```

## 구현 소스
```py
# 퀵 정렬 (Quick Sort)

def quick_sort(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end

	while left <= right:
		while left <= end and array[left] <= array[pivot]:
			left += 1
		
		while right > start and array[right] >= array[pivot]:
			right -= 1
		
		if left > right: # 엇갈렸다면
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면
			array[left], array[right] = array[right], array[left]

		quick_sort(array, start, right-1)
		quick_sort(array, right+1, end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 파이썬의 장점을 살린 구현 소스
```py
def improved_quick_sort(array):
    if len(array) <= 1: return array

    pivot = array[0]
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

	# print(left_side, right_side)

    return improved_quick_sort(left_side) + [pivot] + improved_quick_sort(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
improved_quick_sort(array)
print(array)

'''
[0, 3, 1, 2, 4] [7, 9, 6, 8]
[] [3, 1, 2, 4]
[1, 2] [4]
[] [2]
[6] [9, 8]
[8] []
'''
```

----

<br/>

# 계수 정렬 (Count Sort)
계수 정렬은 **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때** 사용할 수 있는 알고리즘으로, 속도가 매우 빠르다.

> 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000이 넘지 않을 때 효과적으로 사용할 수 있다.

0 이상 100 이하인 성적 데이터를 정렬할 때는 계수 정렬이 효과적이다.
## 구현 소스
```py
# 계수 정렬 (Count Sort)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]): # count[i]의 횟수 만큼 출력
        print(i, end = ' ') # 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

## 시간 복잡도
모든 데이터가 양의 정수이며, 데이터의 개수가 N, 데이터 중 최댓값이 K일 때 계수 정렬은 $O(N+K)$ 의 수행 시간을 보장한다.

## 공간 복잡도
계수 정렬은 때에 따라 심각한 비효율성을 초래할 수 있다.

예를 들어 데이터가 0과 999,999 단 2개만 존재한다면 리스트의 크기가 100만개가 되도록 선언해야 한다. 

따라서 항상 사용할 수 있는 정렬 알고리즘은 아니며, **동일한 값을 가지는 데이터가 여러 개 등장할 때 적합**하다.