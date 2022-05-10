import math

generated_nums = []

def solution(numbers):
    num_list = list(numbers)
    
    size = len(num_list)
    
    for i in range(size):
        visited = [False] * size
        visited[i] = True
        generate(num_list[i], visited, num_list)


    new_num_list = []
    for str_num in generated_nums:
        num = int(str_num)
        if num in new_num_list: continue
        new_num_list.append(num)

    print(new_num_list)

    count = 0
    for num in new_num_list:
        if is_primer_number(int(num)):
            count += 1 

    return count


def generate(str_num, visited, num_list):
    generated_nums.append(str_num)
    for i in range(len(visited)):
        if visited[i]: continue

        new_str = str_num + num_list[i]
        visited[i] = True

        generate(new_str, visited, num_list)


def is_primer_number(x):
    if x == 0 or x == 1: return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True



# print(solution('17'))
print(solution('011'))