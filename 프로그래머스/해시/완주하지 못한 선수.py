def solution(participant, completion):
    participant.sort()
    completion.sort()

    i = 0
    while i < len(completion):
        if participant[i] != completion[i]:
            break
        i = i + 1

    return participant[i]


if __name__ == '__main__':
    p1 = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    c1 = ['josipa', 'filipa', 'marina', 'nikola']

    p2 = ['mislav', 'stanko', 'mislav', 'ana']
    c2 = ['stanko', 'ana', 'mislav']

    answer = solution(p2, c2)
    print(answer)



