# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key = lambda x : x * 3, reverse = True) # for sorting by ASCII
    
    return str(int(''.join(nums)))




print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
