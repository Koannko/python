# 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from pathlib import Path
import pathlib
from random import randint
from unittest import result


def getPolynomial(k):
    result = ''
    for i in range(k, -1, -1):
        n = randint(0, 100)
        if i != k and n != 0 and result != '':
            result += ' + '
        if n > 1:
            if i > 1:
                result += (f'{n}x^{i}')
            elif i == 1:
                result += (f'{n}x')
            else:
                result += (f'{n}')
        elif n == 1:
            if i > 1:
                result += (f'x^{i}')
            elif i == 1:
                result += (f'x')
            else:
                result += (f'1')
    if result.find('x') == -1 or result == '':
        result = '0 = 0'
    else:
        result += ' = 0'
    return result


def writeToFile(data, path):
    with open(path, 'w') as file:
        file.write(data)
        return 0


k = 4
d = 6
path_1 = Path('lesson_2', 'seminar_4', 'homework_4', 'file_1.txt')
path_2 = Path('lesson_2', 'seminar_4', 'homework_4', 'file_2.txt')

writeToFile(getPolynomial(k), path_1)
writeToFile(getPolynomial(d), path_2)
