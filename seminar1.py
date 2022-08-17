# 1. По двум заданным числам проверить является ли одно квадратом второго

# def isSquare(x, y):
#     return x**2 == y or y**2 == x
# print(isSquare(4, 2))


# 2. Найти максимальное из пяти чисел

# l = [1, 2, 3, 5, 7]
# def Task2 (l):
#    return max(l)
# print (Task2(l))


# 3. Вывести на экран числа от -N до N

# def mapNumbers(N):
#     for n in range(-N, N+1, 1):
#         print(n)
#     return 0


# mapNumbers(7)


# 4. Показать первую цифру дробной части числа
# def firstDigitOfFractionalPart(f):
#     return int(f * 10 % 10)


# print(firstDigitOfFractionalPart(1.64))


# 5.Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
# daysOfWeek = ['monday', 'tuesday',
#               'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# def printDayOfWeek(N):
#     return daysOfWeek[(N - 1) % 7]


# print(printDayOfWeek(16))


# 6.Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# def isDivisible(N):
#     return N % 5 == 0 and (N % 2 == 0 or N % 3 == 0) and N % 6 != 0


# print(isDivisible(10))


# 7.Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# def isTrue():
#     case = [0, 0, 0]
#     variablesAmount = 3
#     amount = range(2**10, 2**10 + 2**variablesAmount)
#     for i in range(1, variablesAmount + 1):
#         for n in amount:
#             case[-i] = int(bin(n)[-i])
#             if (not (case[0] or case[1] or case[2])) != (not case[0] and not case[1] and not case[2]):
#                 return False

#     return True


# print(isTrue())


# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

# def getQuarterPlane(x, y):
#     if x >= 0 and y >= 0:
#         return 1
#     elif x < 0 and y >= 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     else:
#         return 4


# print(getQuarterPlane(-3, -4))


# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

# intervals = ['(-Infinity, 0)', '[0, +Infinity)']


# def getValidСoordinates(quarter):
#     if quarter == 1:
#         return ("X belongs to " + intervals[1] + ", Y belongs to " + intervals[1])
#     elif quarter == 2:
#         return ("X belongs to " + intervals[0] + ", Y belongs to " + intervals[1])
#     elif quarter == 3:
#         return ("X belongs to " + intervals[0] + ", Y belongs to " + intervals[0])
#     else:
#         return ("X belongs to " + intervals[1] + ", Y belongs to " + intervals[0])


# print(getValidСoordinates(3))


# 10. Найти расстояние между двумя точками пространства

# def getDistanceBetweenPoints():
#     a = []
#     b = []
#     print('Введите координаты первой точки соответственно: x, y, z')
#     for i in range(3):
#         a.append(int(input()))

#     print('Введите координаты первой точки соответственно: x, y, z')
#     for i in range(3):
#         b.append(int(input()))

#     return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5


# print(getDistanceBetweenPoints())
