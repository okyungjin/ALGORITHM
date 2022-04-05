#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 20분
# 시간 제한 1초

# 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/60058

# 균형잡힌 괄호 문자열의 인덱스 반환
def get_balanced_index(p):
    n_left_bracket = 0
    for i in range(len(p)):
        if p[i] == '(':
            n_left_bracket += 1
        else:
            n_left_bracket -= 1  
        if n_left_bracket == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    n_left_bracket = 0
    for i in p:
        if i == '(':
            n_left_bracket += 1
        else:
             # ) 괄호가 나왔으나 쌍이 맞지 않는 경우
            if n_left_bracket == 0:
                return False
            n_left_bracket -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = get_balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer += u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


# 프로그래머스 제출 시에는 이하 생략
testcase = [
    ('(()())()', '(()())()'),
    (')(', '()'),
    ('()))((()', '()(())()'),
]
for p, result in testcase:
    print(solution(p), end = ' ')
    print(solution(p) == result)

    

    