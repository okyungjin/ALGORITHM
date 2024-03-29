# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

from math import sqrt, ceil

def solution(brown, yellow):
        yellow_width = yellow
        yellow_height = 1

        while yellow_width >= yellow_height:
            # 테두리 개수 비교
            if 2 * (yellow_width + yellow_height) + 4 == brown:
                return [yellow_width + 2, yellow_height + 2]

            yellow_height += 1
            while yellow % yellow_height != 0:
                yellow_height += 1
            yellow_width = yellow // yellow_height


# 22.08.29
class Solve1:
    def solution(brown, yellow):
        total = brown + yellow

        for height in range(3, ceil(sqrt(total)) + 1):
            if total % height != 0: continue
            width = total // height
            if height > width: continue

            if 2 * (width + height) - 4 + (width - 2) * (height - 2) == total and (width - 2) * (height - 2) == yellow:
                return [width, height]




    

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))