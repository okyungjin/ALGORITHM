# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re

def solution(new_id):
    if new_id == '': return 'aaa'

    # step1:
    answer = new_id.lower()

    # step2:
    answer = re.sub('[^a-z0-9-_.]', '', answer)

    # step3:
    answer = re.sub(r'\.+', '.', answer)

    # step4:
    answer = answer.strip('.')

    # step5, 6, 7:
    if answer == '': return 'aaa'
    if len(answer) == 1: return answer * 3
    if len(answer) == 2: return answer + answer[-1]
    if len(answer) > 15: return answer[:15].rstrip('.')
    return answer


testcases = {
    '...!@BaT#*..y.abcdefghijklm..': 'bat.y.abcdefghi',
    'z-+.^.': 'z--',
    "=.=": "aaa",
    "123_.def": "123_.def",
    "abcdefghijklmn.p": "abcdefghijklmn",
}

for new_id, answer in testcases.items():
    print(solution(new_id) == answer, answer, '/', solution(new_id))