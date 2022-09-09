# Bronze 2
# https://www.acmicpc.net/problem/13458

import sys

room_count = int(sys.stdin.readline().rstrip())
student_count_by_room = list(map(int, sys.stdin.readline().split()))
main_watcher, sub_watcher = map(int, sys.stdin.readline().split())

answer = 0
for i in range(len(student_count_by_room)):
    student_count_by_room[i] -= main_watcher
    answer += 1

    if student_count_by_room[i] < 1: continue

    if student_count_by_room[i] % sub_watcher == 0:
        answer += student_count_by_room[i] // sub_watcher
    else:
        answer += student_count_by_room[i] // sub_watcher + 1
        
print(answer)