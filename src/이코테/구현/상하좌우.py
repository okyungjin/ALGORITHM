class Pos:
    def __init__(self, size):
        self.size = size
        self.x = 1
        self.y = 1

    def moveLeft(self):
        if self.y <= 1:
            return
        self.y -= 1

    def moveRight(self):
        if self.y >= self.size:
            return
        self.y += 1

    def moveUp(self):
        if self.x <= 1:
            return
        self.x -= 1

    def moveDown(self):
        if self.y >= self.size:
            return
        self.x += 1

    def toString(self):
        return '{} {}'.format(self.x, self.y)


n = int(input())
moves = input().split()
pos = Pos(n)

for move in moves:
    if move == 'L':
        pos.moveLeft()
    if move == 'R':
        pos.moveRight()
    if move == 'U':
        pos.moveUp()
    if move == 'D':
        pos.moveDown()

print(pos.toString())