def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1

array = ['apple', 'banana', 'mango']
result = sequential_search(array, 'banana')

print(result)