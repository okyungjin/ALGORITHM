# 퀵 정렬 (Quick Sort)

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면
            array[left], array[right] = array[right], array[left]

        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)


def improved_quick_sort(array):
    if len(array) <= 1: return array

    pivot = array[0]
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    print(left_side, right_side)

    return improved_quick_sort(left_side) + [pivot] + improved_quick_sort(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(array, 0, len(array) - 1)

improved_quick_sort(array)
print(array)

'''
[0, 3, 1, 2, 4] [7, 9, 6, 8]
[] [3, 1, 2, 4]
[1, 2] [4]
[] [2]
[6] [9, 8]
[8] []
'''