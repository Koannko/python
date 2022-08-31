# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def getList(N):
#     a = []
#     n = range(0, N)
#     for x in n:
#         a.append((-3)**x)
#     return a


# print(getList(5))

# 12.- Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def getListIndex(N):
#     a = {}
#     n = range(1, N + 1)
#     for x in n:
#         a.append({x}: 3{x} + 1, &x)
#     return a


# print(getListIndex(6))


# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# def amountRepeats(a, b):

#     if len(a) > len(b):
#         maxStr = a
#         minStr = b
#     else:
#         maxStr = b
#         minStr = a

#     count = 0
#     for x in range(len(maxStr)):
#         if maxStr.find(minStr, x, x + len(minStr)) != -1:
#             count += 1

#     return count


# print(amountRepeats('ghghjh', 'g'))

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

# 16. -Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

# def remarkableLimit2(n):
#     series = []
#     for x in range(1, n + 1):
#         series.append((1 + 1/x)**x)
#     return (series[0] + series[n - 1]) / 2 * n


# print(remarkableLimit2(50))

# 17. -Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# from random import randint, randrange


# def getMultipleOfElemsFromFile(N):
#     list1 = []
#     for x in range(0, N):
#         list1.append(randrange(-N, N))
#     print(list1)
#     res = 1
#     with open('file.txt', 'r') as data:
#         for line in data:
#             res *= list1[int(line) % N]

#     return res


# print(getMultipleOfElemsFromFile(10))

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
# def mixListWithGraphicOfFunc(elems):
#     length = len(elems)
#     for x in range(0, length):
#         y = (x**4 + 3 * x**3 - 18 * x**2 + 23 * x - 298) % length
#         a = elems[y]
#         elems[y] = elems[x]
#         elems[x] = a
#     return elems


# print(mixListWithGraphicOfFunc(
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

# Вариант 3. Перевернуть список
# def rev(*params):
#     result = list(params)
#     result = result[::-1]
#     return result
# print(rev(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))


listOfNums = [1, 12, 43, 1, 0, 22, 13, 14, 15, 18]
result = 0
for i in range(len(listOfNums) // 2):
    result += listOfNums[2 * i + 1]
print(result)

# 2i + 1
