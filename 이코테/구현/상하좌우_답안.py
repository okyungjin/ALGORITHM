n = int(input())
moves = input().split()

xpos, ypos = 1, 1

# L, R, U, D 순서대로
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(len(move_types)):
        if move == move_types[i]:
            next_xpos = xpos + dx[i]
            next_ypos = ypos + dy[i]

        if next_xpos < 1 or next_xpos > n or next_ypos < 1 or next_ypos > n:
            continue

        x, y = next_xpos, next_ypos

print(xpos, ypos)
