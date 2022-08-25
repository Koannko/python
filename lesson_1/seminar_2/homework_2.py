# 14. -Подсчитать сумму цифр в вещественном числе.

# def getAmountOfDigits(a):
#     numLength = len(str(a))
#     sum = 0
#     for x in range(0, numLength):
#         if (str(a)[x] != '.'):
#             sum += int(str(a)[x])
#     return numLength, sum

# print(getAmountOfDigits(1.33))
# print(getAmountOfDigits(126))

# 15. -Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# def factorial(N):
#     a = [1]
#     for x in range(1, N):
#         a.append(a[x - 1] * (x + 1))
#     return a


# print(factorial(8))

# 18. Реализовать алгоритм перемешивания списка.

# # Вариант 1. Находить псевдо рандомное число и менять элемент списка
# с индексом x и элемент с индексом полученным случайно

# def mixList(*elems):
#     res = list(elems)
#     length = len(elems)
#     for x in range(0, length):
#         randNum = randint(0, length - 1)
#         a = res[randNum]
#         res[randNum] = res[x]
#         res[x] = a
#     return res
# print(mixList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

# # Вариант 2. Находить числа с помощью графика некоторой кривой и менять пары элементов местами
# def mixListWithGraphicOfFunc(*elems):
#     res = list(elems)
#     length = len(elems)
#     for x in range(0, length):
#         y = (x**4 + 3 * x**3 - 18 * x**2 + 23 * x - 298) % length
#         a = res[y]
#         res[y] = res[x]
#         res[x] = a
#     return res
# print(mixListWithGraphicOfFunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

# Вариант 3. Перевернуть список
# def rev(*params):
#     result = list(params)
#     result = result[::-1]
#     return result
# print(rev(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
