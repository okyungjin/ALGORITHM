# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    stack = [s[0]]

    for char in s[1:]:
        if not stack:
            stack.append(char)
            continue
            
        top = stack[-1]

        if top == '(' and char == ')': stack.pop()
        else: stack.append(char)

    return len(stack) == 0



print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))