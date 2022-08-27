# ALGORITHM

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
> **두 자리일때만 유효하여 업데이트 필요함**
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