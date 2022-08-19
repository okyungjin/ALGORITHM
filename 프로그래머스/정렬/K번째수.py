# Level 1
# https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for cmd in commands:
        [start, end, k] = cmd
        sliced = array[start-1:end]
        sliced.sort()
        answer.append(sliced[k - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))