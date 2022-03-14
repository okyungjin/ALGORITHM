import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

# n: 배열의 길이
# k: 최대 k번의 바꿔치기 가능
# 배열 A의 모든 원소 합의 최댓값

n, k = map(int, f.readline().split())

listA = list(map(int, f.readline().split()))
listB = list(map(int, f.readline().split()))

listA.sort(reverse=True)
listB.sort(reverse=True)

result = 0
for i in range(n-k):
    result += listA[i]

for i in range(k):
    result += listB[i]


print(result)
        

        
