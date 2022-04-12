#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 2초

# https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline

data = '0001100'

def zeroToOne(string):
    result = ''
    for s in string:
        if s == '0': result += '1'
        else: result += '1'
    return result

def oneToZero(string):
    result = ''
    for s in string:
        if s == '1': result += '0'
        else: result += '0'
    return result


print(zeroToOne(data))
print(oneToZero(data))

    
    

