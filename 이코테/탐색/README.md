- [순차 탐색 (Sequential Search)](#순차-탐색-sequential-search)
  - [구현 소스](#구현-소스)
- [이진 탐색 (Binary Search)](#이진-탐색-binary-search)
  - [과정](#과정)
  - [시간 복잡도](#시간-복잡도)
  - [구현](#구현)
    - [재귀 함수 사용](#재귀-함수-사용)
    - [반복문 사용](#반복문-사용)
    - [빠르게 입력 받기](#빠르게-입력-받기)


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
```py
def rec_binsearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2;

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return rec_binsearch(array, target, start, mid - 1)
    else:
        return rec_binsearch(array, target, mid + 1, end)

    
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = int(input())

result = rec_binsearch(array, target, 0, len(array) - 1)

if result == None:
    print('There is no element matching the input value.')
else:
    print(result + 1)
```

### 반복문 사용
```py
def loop_binsearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid;
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None;

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = int(input())

result = loop_binsearch(array, target, 0, len(array) - 1)

if result == None:
    print('There is no element matching the input value.')
else:
    print(result + 1)
```

> **탐색 범위가 20,000,000 (2천만)을 넘어가면 이진 탐색으로 문제에 접근해보자.**
> 처리해야 할 데이터가 10,000,000 (천만)을 넘어가면 이진 탐색과 같이 $O(logN)$의 속도를 내야하는 알고리즘을 적용해야 하는 경우가 많다.

### 빠르게 입력 받기

이진 탐색 문제는 입력 데이터가 많거나 탐색 범위가 매우 넓은 편이다.
입력 데이터의 개수가 많을 때 `input()` 함수를 사용하면 동작 속도가 느려져 시간 초과로 오답 판정을 받을 수 있다.

입력 데이터가 많은 문제는 `sys` 라이브러리의 `readline()` 함수를 이용하면 시간 초과를 피할 수 있다.

```py
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)
```
입력 후 엔터가 줄 바꿈 기호(`\n`)로 변환되므로, `sys` 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 `rstrip()` 을 꼭 적어주도록 한다.