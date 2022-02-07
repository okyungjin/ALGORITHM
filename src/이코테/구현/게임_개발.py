def turnLeft(direction):
    return (direction + 3) % 4


height, width = map(int, input().split())  # n, m

y, x, cur_dir = map(int, input().split())

# 방향
#  0
# 3  1
#  2

left_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]
maps = []

for _ in range(height):
    maps.append(list(map(int, input().split())))

maps[x][y] = 1

count = 1
while True:
    flatted_maps = []
    for m in maps:
        flatted_maps += m

    if 0 not in flatted_maps:
        break

    nx = x + left_pos[cur_dir][0]
    ny = y + left_pos[cur_dir][1]

    if maps[nx][ny] == 0:
        x = nx
        y = ny
        maps[x][y] = 1
        count += 1

    cur_dir = turnLeft(cur_dir)

print(count)

