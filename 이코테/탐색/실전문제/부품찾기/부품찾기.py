import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

def binsearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2;
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(f.readline())
componets = list(map(int, f.readline().split()))

m = int(f.readline())
orders = list(map(int, f.readline().split()))

componets.sort()

for order in orders:
    result = binsearch(componets, order, 0, n - 1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

