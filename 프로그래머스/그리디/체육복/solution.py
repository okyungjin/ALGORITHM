def solution(n, lost, reserve):
    counts = [1] * (n + 1)

    for cnt in lost:
        counts[cnt] -= 1

    for cnt in reserve:
        counts[cnt] += 1

    for i in range(1, n):
        if counts[i] == 2:
            if counts[i - 1] == 0 and i - 1 != 0:
                counts[i] -= 1
                counts[i - 1] += 1
                continue
            elif counts[i + 1] == 1:
                counts[i] -= 1
                counts[i + 1] += 1
                
    if counts[n] == 2:
        counts[n] -= 1
        counts[n - 1] += 1

    answer = 0
    for i in range(1, n + 1):
        if counts[i] >= 1:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

