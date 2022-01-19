def solution(phone_book):
    phone_book.sort()

    i = 0
    while i < len(phone_book):
        if i == len(phone_book) - 1:
            return True
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        i = i + 1


if __name__ == '__main__':
    phoneBook = [['119', '97674223', '1195524421'], ['123', '456', '789'], ['12', '123', '1235', '567', '88']]
    for pb in phoneBook:
        print(solution(pb))
