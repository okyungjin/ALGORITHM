# 성적이 낮은 순서로 학생 출력하기

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

n = int(f.readline())

scores = []

for _ in range(n):
    name, score = f.readline().split()
    scores.append((name, int(score)))

scores = sorted(scores, key=lambda s: s[1]) # s[1] 오름차순

 # s[1] 내림차순으로 정렬
 # scores = sorted(scores, key=lambda s: s[1], reverse=True)

for score in scores:
    print(score[0], end = ' ')

