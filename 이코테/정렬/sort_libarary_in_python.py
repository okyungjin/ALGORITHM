

# # sorted
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# result = sorted(array)

# print(array) # [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# sort
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array.sort()
# print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# key 활용
array = [('banana', 2), ('apple', 5), ('mango', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result) # [('banana', 2), ('mango', 3), ('apple', 5)]