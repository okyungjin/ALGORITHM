# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    graph = generate_2d_rectangle_filled_with_ascending_numbers(rows, columns)

    for ltx, lty, rbx, rby in queries:
        # move position for indexing
        ltx -= 1; lty -= 1; rbx -= 1; rby -= 1

        upper_right_num = graph[ltx][rby] # 조각 하나 빼기
        min_num = upper_right_num # init min_num

        # Rotate top
        for y in range(rby - 1, lty - 1, -1):
            min_num = min(min_num, graph[ltx][y])
            if y + 1 < columns:
                graph[ltx][y + 1] = graph[ltx][y]

        # Rotate left
        for x in range(ltx + 1, rbx + 1):
            min_num = min(min_num, graph[x][lty])
            if x - 1 >= 0:
                graph[x - 1][lty] = graph[x][lty]

        # Rotate bottom
        for y in range(lty + 1, rby + 1):
            min_num = min(min_num, graph[rbx][y])
            if y - 1 >= 0:
                graph[rbx][y - 1] = graph[rbx][y]

        # Rotate right
        for x in range(rbx - 1, ltx - 1, -1):
            min_num = min(min_num, graph[x][rby])
            if x + 1 < rows:
                graph[x + 1][rby] = graph[x][rby]

        # 뺀 조각 끼우기
        graph[ltx + 1][rby] = upper_right_num
        answer.append(min_num)

    return answer


''' Generate 2d retangle fiiled with ascending numbers '''
def generate_2d_rectangle_filled_with_ascending_numbers(n_rows, n_cols):
    return [[r * n_cols + c + 1 for c in range(n_cols)] for r in range(n_rows)]

    ''' Transpose of matrix using nested loops
    graph = [[0] * n_cols for r in range(n_rows)]
    for r in range(n_rows):
        for c in range(n_cols):
            graph[r][c] = r * n_cols + c + 1
    '''
    

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



print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]])) # [1]

''' [Unsed] Slice rectangle '''
'''
def slice_rectangle_based_on_upper_left_point_and_lower_right_point(graph: List[List[int]], upper_left: Point, lower_right: Point) -> List[List[int]]:
    res = []
    for row in range(upper_left.x - 1, lower_right.x):
        res.append(graph[row][upper_left.y - 1:lower_right.y])
    return res


def rotate_number(graph: List[List[int]]) -> List[List[int]]:
    return [[]]
'''