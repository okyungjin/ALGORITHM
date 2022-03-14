import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')


n = int(f.readline())

array = []
for _ in range(n):
    array.append(int(f.readline()))

sortedArr = sorted(array, reverse=True)

for i in sortedArr:
    print(i, end = ' ')