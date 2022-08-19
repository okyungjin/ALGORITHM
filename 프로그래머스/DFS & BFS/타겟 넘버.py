def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer


answer = 0
def dfs(numbers, target, result, cnt):
    global answer
    if cnt == len(numbers):
        if result == target:
            answer += 1
        return
    
    dfs(numbers, target, result + numbers[cnt], cnt + 1)
    dfs(numbers, target, result - numbers[cnt], cnt + 1)


# print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1]	, 4))