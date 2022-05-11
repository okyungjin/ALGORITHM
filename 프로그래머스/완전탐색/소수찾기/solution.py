import math
from itertools import permutations


def solution(numbers):
    answer = []
    nums = list(numbers)
    perm = []

    for i in range(1, len(numbers) + 1):
        perm += list(permutations(nums, i))
    new_nums = [int(('').join(p)) for p in perm]
    
    for num in new_nums:
        if is_prime_number(num):
            answer.append(num)
    return len(set(answer))
    
        
def is_prime_number(x):
    if x < 2: return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# print(solution('17'))
# print(solution('011'))