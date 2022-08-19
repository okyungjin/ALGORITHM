def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    counts = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            idx = i % len(patterns[j])
            if answers[i] == patterns[j][idx]:
                counts[j] += 1


    max_count = max(counts)

    answer = []
    for i in range(len(counts)):
        if counts[i] == max_count:
            answer.append(i + 1)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
     