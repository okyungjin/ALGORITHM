from collections import deque

def solution(people, limit):
    answer = 0
    sorted_people = sorted(people)

    left = 0
    right = len(people) - 1

    while left <= right:
        if sorted_people[left] + sorted_people[right] <= limit:
            left += 1
        right -= 1
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3
