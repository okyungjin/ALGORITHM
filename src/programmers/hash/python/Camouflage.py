def solution(clothes):
    closet = {}
    result = 1
    
    for elem in clothes:
        clothesType = elem[1]
        clothesName = elem[0]
        if clothesType in closet:
            closet[clothesType].append(clothesName)
        else:
            closet[clothesType] = [clothesName]

    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1


if __name__ == '__main__':
    clothes_arr = [['yellowhat', 'headgear'], ['bluesunglasses', 'eyewear'], ['green_turban', 'headgear']]
    print(solution(clothes_arr))
