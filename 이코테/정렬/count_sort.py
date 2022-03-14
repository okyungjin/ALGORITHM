# 계수 정렬 (Count Sort)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]): # count[i]의 횟수 만큼 출력
        print(i, end = ' ') # 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
