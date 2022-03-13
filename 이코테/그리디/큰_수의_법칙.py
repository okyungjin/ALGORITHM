n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

max1 = arr[0]
max2 = arr[1]

_sum = 0
count = k

while m > 0:
    if count == 0:
        _sum += max2
        count = k
        m -= 1
    else:
        _sum += max1 * (k if m > k else m)
        count -= k if m > k else m
        m -= k


print(_sum)
