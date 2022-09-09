# Bronze 1
# https://www.acmicpc.net/problem/2309

import sys

SUM_OF_DWARF_HEIGHT = 100
dwarfs = []

for _ in range(9):
    dwarfs.append(int(sys.stdin.readline().rstrip()))


def find_extra_dwarf(dwarf):
    for i in range(len(dwarfs) - 1):
        for j in range(i + 1, len(dwarfs)):
            if dwarfs[i] + dwarfs[j] == extra_height:
                return i, j
                

extra_height = sum(dwarfs) - SUM_OF_DWARF_HEIGHT
i, j = find_extra_dwarf(dwarfs)
dwarfs.pop(i)
dwarfs.pop(j - 1)
dwarfs.sort()

for dwarf in dwarfs:
    print(dwarf)
