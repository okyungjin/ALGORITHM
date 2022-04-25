ans = 0


def solution(numbers, target):
    dfs(numbers[0], target, 0, numbers)
    dfs(-numbers[0], target, 0, numbers)
    return ans


def dfs(result, target, idx, numbers):
    global ans

    if idx == len(numbers) - 1:
        if result == target:
            ans += 1
            return
        else:
            return

    dfs(result + numbers[idx + 1], target, idx + 1, numbers)
    dfs(result - numbers[idx + 1], target, idx + 1, numbers)


if __name__ == '__main__':
    _numbers = [1, 1, 1, 1, 1]
    _target = 3
    _answer = solution(_numbers, _target)
    print(_answer)
