def solution(arr):
    res = []
    
    for i in range(len(arr)):
        if i == 0: res.append(arr[i])
        elif arr[i] != arr[i-1]: res.append(arr[i])

    return res