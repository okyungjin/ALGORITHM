#-*-coding:utf-8-*-

# 난이도 1.5
# 풀이 시간 40분
# 시간 제한 1초

# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    new_lock = generateNewLock(key, lock)
    size = len(new_lock) - len(key) + 1
    for i in range(size):
        for j in range(size):
            if checkIsKeyValid(i, j, size, key, new_lock):
                return True
    return False


def rotateClockWise90(arr):
    return list(zip(*arr[::-1]))


def generateNewLock(key, lock):
    lock_size = len(lock)
    key_size = len(key)
    new_lock_size = lock_size + (key_size - 1) * 2
    new_lock = [[0 for _ in range(new_lock_size)] for _ in range(new_lock_size)]

    for i in range(key_size - 1, key_size + lock_size - 1):
        for j in range(key_size - 1, key_size + lock_size - 1):
            new_lock[i][j] = lock[lock_size - i - 1][lock_size - j - 1]
    return new_lock;

    
def checkIsKeyValid(i, j, size, key, new_lock):
    for k in range(len(key)):
        for l in range(len(key)):
            xpos = i + k
            ypos = j + l
            if new_lock[xpos][ypos] == 1 and key[k][l] == 1:
                return False
            if new_lock[xpos][ypos] == 0 and key[k][l] == 1:
                new_lock[xpos][ypos] = key[k][l]
            
    for a in range(size):
        for b in range(size):
            if new_lock[i][j] != 1:
                return False
    return True

            
            
key = [[0, 0, 0],[1, 0, 0],[0, 1, 1]]
lock = [[1, 1, 1],[1, 1, 0],[1, 0, 1]]

# key = [[0, 0, 0],[1, 0, 0],[0, 1, 1]]
# lock = [[1, 1, 1, 0, 0],[1, 1, 0, 1, 1],[1, 0, 1, 0, 1],[1, 0, 1, 0, 1],[1, 0, 1, 0, 1]]

print(solution(key, lock))



