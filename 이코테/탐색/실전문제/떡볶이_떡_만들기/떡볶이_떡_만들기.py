import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

n, m = map(int, f.readline().split())
dduks = list(map(int, f.readline().split()))

def get_sum(array, height):
    result = 0
    for elem in array:
        if elem > height:
            result += elem - height
    return result


def binsearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2;
        
        res = get_sum(array, mid);
        
        if res == target:
            return mid
        elif res > target:
            start = mid + 1
        else:
            end = mid - 1

    return None;

dduks.sort()

res = binsearch(dduks, m, 0, dduks[-1])
print(res)