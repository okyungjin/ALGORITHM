def loop_binsearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid;
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None;

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = int(input())

result = loop_binsearch(array, target, 0, len(array) - 1)

if result == None:
    print('There is no element matching the input value.')
else:
    print(result + 1)