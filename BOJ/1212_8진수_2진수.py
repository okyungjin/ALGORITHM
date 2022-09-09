# Bronze 2
# https://www.acmicpc.net/problem/1212

import sys

OCTAL_PREFIX = '0o'
BINARY_PREFIX = '0b'

decimal_int = int(OCTAL_PREFIX + sys.stdin.readline().rstrip(), 8)
print(bin(decimal_int).replace('0b', ''))
