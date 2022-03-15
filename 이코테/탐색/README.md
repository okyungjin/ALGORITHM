- [순차 탐색 (Sequential Search)](#순차-탐색-sequential-search)
  - [구현 소스](#구현-소스)
- [이진 탐색 (Binary Search)](#이진-탐색-binary-search)
  - [과정](#과정)
  - [시간 복잡도](#시간-복잡도)
  - [구현](#구현)
    - [재귀 함수 사용](#재귀-함수-사용)
    - [반복문 사용](#반복문-사용)


----

# 순차 탐색 (Sequential Search)
리스트에서 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법이다.
보통 **정렬되지 않은 리스트**에서 데이터를 찾아야 할 때 사용한다.

## 구현 소스
```py
def sequential_search(array, target):
    for i in range(len(arddray)):
        if array[i] == target:
            return i + 1

array = ['apple', 'banana', 'mango']
result = sequential_search(array, 'banana')

print(result)
```

----

# 이진 탐색 (Binary Search)

> 이진 탐색은 **배열 내부의 데이터가 이미 정렬되어 있어야만 사용할 수 있는** 알고리즘이다.

이진 탐색은 탐색 범위를 절반씩 좁혀 탐색하는 특징이 있다.

## 과정
`[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]` 에서 `4` 라는 원소의 index를 찾으려고 한다.


```py

#1: start와 end의 index를 합해 반으로 나눈 지점을 mid로 잡는다. 0 + 9 / 2 = 4.5에서 소수점을 날려 mid는 4가 된다. 
 st       mid             end
[0] 2 4 6 [8] 10 12 14 16 [18]


#2: array[4]인 8은 target 데이터인 4보다 크므로
end = mid - 1 # 설정한다.
st  mid   end
[0] [2] 4 [6] 8 10 12 14 16 18

mid = 0 + 3 / 2 = 1.5 = 1

#3: array[1]는 target 데이터인 4보다 작으므로
start = mid # 설정한다.
     s
     m   e    
0 2 [4] [6] 8 10 12 14 16 18


#4: array[2]는 target 데이터와 일치하므로 탐색을 종료한다.
```

## 시간 복잡도
이진 탐색은 한 번 확인할 때마다 탐색할 원소의 개수가 절반으로 줄어든다는 점에서 $O(logN)$의 시간 복잡도를 갖는다.

## 구현 
### 재귀 함수 사용
```py```

### 반복문 사용
```py```

----