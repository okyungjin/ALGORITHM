#-*-coding:utf-8-*-

# 난이도 1.5
# 풀이 시간 30분
# 시간 제한 1초

# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

def solution(s):
    min_len = len(s)
    for i in range(1, len(s) // 2 + 1):
        new_s = ''
        cnt = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if (cnt != 1):
                    new_s += str(cnt)
                new_s += s[j:j+i]
                cnt = 1

        min_len = min(min_len, len(new_s))
    return min_len


test_case = int(f.readline().rstrip())
for _ in range(test_case):
    s, answer = f.readline().split()
    print(int(answer) == solution(s))

