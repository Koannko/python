# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multiplePairOfNums(listOfNums):
    result = []
    lengthOfList = len(listOfNums)
    for i in range(lengthOfList // 2 + lengthOfList % 2):
        result.append(listOfNums[i] * listOfNums[lengthOfList - 1 - i])
    return result


print(multiplePairOfNums([1, 12, 43, 1, 0]))  # => [0, 12, 1849]
print(multiplePairOfNums([4, 2, 33, 12, 15, 2]))  # => [8, 30, 396]
