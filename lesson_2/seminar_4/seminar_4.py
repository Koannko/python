# 27. Строка содержит набор чисел. Показать большее и меньшее число
# def minAndMaxInStr(strOfNum: str) -> tuple:
#     listOfNum = strOfNum.split()
#     li = [int(el) for el in listOfNum]
#     return min(li), max(li)


# print(minAndMaxInStr('234 34 78 349'))

# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0.
# a. Математикой


def solveSquareEquation(equation: str):
    lenOfEquation = len(equation)
    for i in range(0, lenOfEquation):
        A = equation[i:(i+4)]
        if A == 'x**2':
            res = int(equation[0:i])

    return res


# print(solveSquareEquation('x**2 + 4x - 5 = 0'))


print(solveSquareEquation('21x**2 - 3x + 1 = 0'))
# Используя дополнительные библиотеки*
# Найти НОК двух чисел
# Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10
#       30*** , Подумать, что если точность вычисления до 1000 знаков после запятой
# Составить список простых множителей натурального числа N
