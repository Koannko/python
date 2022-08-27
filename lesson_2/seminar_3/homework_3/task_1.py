# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sumOfNumsInOddPositions(listOfNums):
    result = 0
    for i in range(len(listOfNums) // 2):
        result += listOfNums[2 * i + 1]
    return result


print(sumOfNumsInOddPositions([1, 12, 43, 1, 0, 22]))  # => 35
print(sumOfNumsInOddPositions([4, 2, 33, 12, 15, 2, 31, 12, 25]))  # => 28
