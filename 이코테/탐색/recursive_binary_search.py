def rec_binsearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return rec_binsearch(array, target, start, mid - 1)
    else:
        return rec_binsearch(array, target, mid + 1, end)

    
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = int(input())

result = rec_binsearch(array, target, 0, len(array) - 1)

if result == None:
    print('There is no element matching the input value.')
else:
    print(result + 1)


