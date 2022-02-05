n, k = map(int, input().split())

result = n % k
n -= result

while n > 1:
    n //= k
    result += 1

print(result)
