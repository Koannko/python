# 3. Вывести на экран числа от -N до N

# def mapNumbers(N):
#     return [n for n in range(-N, N+1, 1)]


# print(mapNumbers(7))

# 5.Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# def printDayOfWeek(N):
#     day = ['monday', 'tuesday',
#            'wednesday', 'thursday', 'friday', 'saturday', 'sunday'][(N - 1) % 7]
#     return f'{day}{((int(is_weekend(N))) * ", " + (int(is_weekend(N))) * "weekend")}'


# def is_weekend(N):
#     return (N - 1) % 7 > 4


# print(printDayOfWeek(16))
# print(printDayOfWeek(6))
# print(printDayOfWeek(5))
# print(printDayOfWeek(3))


# 6.Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
# from math import fsum


# def decision(N):
#     return int(N % 5 == 0) and fsum([(int(N % i == 0)) for i in [2, 3, 5]]) % 3 != 0


# print(decision(5))
# print(decision(10))
# print(decision(15))
# print(decision(30))

# 14. -Подсчитать сумму цифр в вещественном числе.

# def getAmountOfDigits(a):
#     return len(''.join(str(a).split('.')))


# print(getAmountOfDigits(1.33))
# print(getAmountOfDigits(126))

# 15. -Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# def factorial(N):
#     if N == 1:
#         return 1
#     return factorial(N - 1) * N


# def get_factorials_from_1_to_N(N):
#     return [factorial(i) for i in range(1, N + 1)]


# print(get_factorials_from_1_to_N(8))

# 18. Реализовать алгоритм перемешивания списка.
# from random import randint


# def mixList(elems):
#     for i in range(len(elems)):
#         j = randint(i, len(elems) - 1)
#         elems[i], elems[j] = elems[j], elems[i]
#     return elems


# print(mixList([51, 32, 83, 14, 75]))


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# from math import fsum


# def sumOfNumsInOddPositions(listOfNums):
#     return int(fsum([listOfNums[x] for x in range(0, len(listOfNums)) if x % 2 == 1]))


# print(sumOfNumsInOddPositions([1, 12, 43, 1, 0, 22]))  # => 35
# print(sumOfNumsInOddPositions([4, 2, 33, 12, 15, 2, 31, 12, 25]))  # => 28


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def multiplePairOfNums(listOfNums):
#     lengthOfList = len(listOfNums)
#     return [listOfNums[i] * listOfNums[lengthOfList - 1 - i] for i in range((lengthOfList - 1) // 2 + 1)]


# print(multiplePairOfNums([1, 12, 43, 1, 0]))  # => [0, 12, 1849]
# print(multiplePairOfNums([4, 2, 33, 12, 15, 2]))  # => [8, 30, 396]


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# import math


# def difMaxAndMinFractionalParts(listOfFloats):
#     fractionalParts = [round(math.modf(num)[0], 10) for num in listOfFloats]
#     return max(fractionalParts) - min(fractionalParts)


# print(difMaxAndMinFractionalParts([1.1, 1.4, 1.01]))  # => 0.39
# print(difMaxAndMinFractionalParts([1.1, 1.2, 3.1, 1.01]))  # => 0.19



