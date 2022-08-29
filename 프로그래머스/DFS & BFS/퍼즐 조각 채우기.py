# Level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/84021?language=python3

from typing import List
import itertools
import copy

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
MAX_BOARD_SIZE = 51

def solution(game_board, table):
    size = len(table)
    empty_size_in_game_board = list(itertools.chain(*game_board)).count(0)

    # 조각 수 별 퍼즐 조각들
    puzzle_pieces_by_piece = dict()

    # puzzle 조각 추출하기
    for x in range(size):
        for y in range(size):
            cords = get_puzzle_cords(table, size, x, y, [])
            if cords is None: continue

            puzzle_size = len(cords)
            cords = move_puzzle_closer_to_starting_point(cords)
            if puzzle_size in puzzle_pieces_by_piece:
                puzzle_pieces_by_piece[puzzle_size].append(cords)
            else:
                puzzle_pieces_by_piece[puzzle_size] = [cords]

    # game_bard에서 빈 공간에 추출한 puzzle 맞추기                
    for x in range(size):
        for y in range(size):
            empty_space = get_empty_spaces_cords(game_board, size, x, y, [])
            if empty_space is None: continue

            empty_space = move_puzzle_closer_to_starting_point(empty_space)
            empty_size = len(empty_space)

            if empty_size not in puzzle_pieces_by_piece: continue
            for i in range(len(puzzle_pieces_by_piece[empty_size])):
                puzzle_graph = convert_cords_to_graph(puzzle_pieces_by_piece[empty_size][i])
                
                for _ in range(4):
                    copied_puzzle_graph = rotate_rectangle_clockwise(copy.deepcopy(puzzle_graph), True)
                    for empty_x, empty_y in empty_space:
                        if empty_x < len(copied_puzzle_graph) and empty_y < len(copied_puzzle_graph[0]):
                            copied_puzzle_graph[empty_x][empty_y] = 1
                    if list(itertools.chain(*copied_puzzle_graph)).count(0) == 0:
                        empty_size_in_game_board -= empty_size
                        puzzle_pieces_by_piece[empty_size].pop(i)
                        break

    print(empty_size_in_game_board)
            # if es in puzzle_pieces_by_piece:                    
            #     for i in range(len(puzzle_pieces_by_piece[es])):
            #         print(puzzle_pieces_by_piece[es])
            #         puzzle = puzzle_pieces_by_piece[es][i]

            #         # FIXME: Simplify logic
            #         puzzle_graph = convert_cords_to_graph(puzzle)
                    
            #         for empty_x, empty_y in empty_space:
            #             try:
            #                 puzzle_graph[empty_x][empty_y] = 0
            #             except:
            #                 continue

            #         flatted = list(itertools.chain(puzzle_graph))
            #         print(flatted)
            #         if flatted.count(1) == 0:
            #             puzzle_pieces_by_piece[es] = puzzle_pieces_by_piece[es].pop(i)
                    
    # game_bard 빈 공간 다 돌면서 조각 끼우기
    ## 1) 빈 공간 탐색
    ## 2) 조각 회전하면서 끼우기 -> move_piece_close_to_starting_point

    # 정답: size ** 2 - 남은 1의 개수
    return 1



def convert_cords_to_graph(cords):
    res = [[0]]
    print(cords)

    for x, y in cords:
        while max(x, y) >= len(res):
            for row in res:
                row.append(0)
            res.append([0] * len(res[0]))
        res[x][y] = 1

    return res

def get_puzzle_cords(table, size, x, y, cords):
    if table[x][y] == 0: return

    table[x][y] = 0 # 방문처리
    cords.append((x, y))

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < size and 0 <= ny < size and table[nx][ny] == 1:
            # print(cords)
            get_puzzle_cords(table, size, nx, ny, cords)

    return cords if cords is not [] else None


def get_empty_spaces_cords(game_board, size, x, y, cords):
    if game_board[x][y] == 1: return

    game_board[x][y] = 1 # 방문처리
    cords.append((x, y))

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < size and 0 <= ny < size and game_board[nx][ny] == 0:
            # print(cords)
            get_empty_spaces_cords(game_board, size, nx, ny, cords)

    return cords if cords is not [] else None


def move_puzzle_closer_to_starting_point(puzzle_cords):
    if len(puzzle_cords) == 0: return []

    min_x, min_y = MAX_BOARD_SIZE, MAX_BOARD_SIZE
    for x, y in puzzle_cords:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    
    for i in range(len(puzzle_cords)):
        origin_cord = puzzle_cords[i]
        puzzle_cords[i] = (origin_cord[0] - min_x, origin_cord[1] - min_y)

    return puzzle_cords





'''
- dfs
- (0,0)에 가깝게 붙여야 함
- puzzle_pieces_by_piece에 할당
'''
def extract_puzzle_pieces(table, size, x, y, puzzle_piece):
    

    # if table[x][y] == 1:
    #     # 사이즈 작으면 늘리기
    #     while len(puzzle_piece) >= max(x, y):


    #     puzzle_piece[x][y] = 1

    #     for dx, dy in directions:
    #         nx = x + dx
    #         ny = y + dy

    #         if 0 <= nx < size and 0 <= ny < size:
    #             pass

        

        return []


# def dfs(graph: List[List[int]], cur: Point, n: int, target: int) -> bool:
    # ret = [position]
    
    # for dx, dy in range(len(directions)):
    #     nx = cur.x + dx
    #     ny = cur.y + dy
        
    #     if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
    #         graph[nx][ny] = 2
    #         ret = ret + dfs(graph, nx, ny, [position[0]+dic[i][0], position[1]+dic[i][1]], n, num)
    # return True


def rotate_rectangle_clockwise(rectangle, is_square = False):
    if not rectangle: return [[]]

    height = len(rectangle)
    width = height if is_square else len(rectangle[0])
    rotated = [[0] * height for _ in range(width)]

    # _col: index of colum / _row: index of row
    for _col in range(width):
        for _row in range(height):
            rotated[_col][height - _row - 1] = rectangle[_row][_col]

    return rotated


''' Print 2d list'''
def print_2d_list(arr: List[List[int]]) -> None:
    for row in arr:
        for col in row:
            print(col, end = ' ')
        print()
    print()




print(solution([
    [1,1,0,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]], [

        [1,0,0,1,1,0],
        [1,0,1,0,1,0],
        [0,1,1,0,1,1],
        [0,0,1,0,0,0],
        [1,1,0,1,1,0],
        [0,1,0,0,0,0]])) # 14


# print(solution([
#     [0,0,0],
#     [1,1,0],
#     [1,1,1]], [

#         [1,1,1],
#         [1,0,0],
#         [0,0,0]])) # 0