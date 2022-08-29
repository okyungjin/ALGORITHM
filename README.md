# ALGORITHM
- [그래프](#그래프)
  - [1부터 채워진 2차원 그래프 생성](#1부터-채워진-2차원-그래프-생성)
  - [2차원 그래프 출력](#2차원-그래프-출력)
  - [2차원 그래프 slice](#2차원-그래프-slice)
  - [2차원 좌표 자료구조](#2차원-좌표-자료구조)
  - [2차원 그래프 회전](#2차원-그래프-회전)
## 그래프
### 1부터 채워진 2차원 그래프 생성
```py
''' Generate 2d retangle fiiled with ascending numbers '''
def generate_2d_rectangle_filled_with_ascending_numbers(n_rows, n_cols):
    return [[r * n_cols + c + 1 for c in range(n_cols)] for r in range(n_rows)]
```

다음과 같이 펼쳐서 사용할 수도 있다.
```py
''' Transpose of matrix using nested loops '''
graph = [[0] * n_cols for r in range(n_rows)]
for r in range(n_rows):
    for c in range(n_cols):
        graph[r][c] = r * n_cols + c + 1
    
```

### 2차원 그래프 출력
#### 원소가 한 자리 수
```py
''' Print 2d list'''
def print_2d_list(arr: List[List[int]]) -> None:
    for row in arr:
        for col in row:
            print(col, end = ' ')
        print()
    print()
```
#### 원소가 두 자리 수

```py
def print_2d_graph(graph):
    print('======= graph =======')
    for row in graph:
        res = ''
        for col in row:
            col = str(col)
            res += col + ' ' if len(col) > 1 else ' ' + col + ' '
        print(res)
    print('======= graph =======')        
    print()
```

### 2차원 그래프 slice
```py
''' Slice rectangle '''
def slice_rectangle_based_on_upper_left_point_and_lower_right_point(graph: List[List[int]], upper_left: Point, lower_right: Point) -> List[List[int]]:
    res = []
    for row in range(upper_left.x - 1, lower_right.x):
        res.append(graph[row][upper_left.y - 1:lower_right.y])
    return res
```

### 2차원 좌표 자료구조
```py
''' [Data Structure] 2D Point '''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
```

### 2차원 그래프 회전
#### 시계 방향
```
[example]
1 2      5 3 1
3 4  =>  6 4 2
5 6

[roated pos]
(0,0) (0,1)      (2,0) (1,0) (0,0)
(1,0) (1,1)  =>  (2,1) (1,1) (0,1)
(2,0) (2,1)      
                 -- origin pos --
                 (0,0) (0,1) (0,2)
                 (1,0) (1,1) (1,2)
```
```py
''' Rotate Rectangle '''
def rotate_rectangle_clockwise(rectangle: List[List[int]], is_square: bool = False) -> List[List[int]]:
    if not rectangle: return [[]]

    height = len(rectangle)
    width = height if is_square else len(rectangle[0])
    rotated = [[0] * height for _ in range(width)]

    # _col: index of colum / _row: index of row
    for _col in range(width):
        for _row in range(height):
            rotated[_col][height - _row - 1] = rectangle[_row][_col]

    return rotated
```