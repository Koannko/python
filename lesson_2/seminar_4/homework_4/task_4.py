# 4**. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import pathlib
from pathlib import Path


def readPolinom(path):
    with open(path, 'r') as data:
        polynom = data.read()
        return polynom


def getNumeratorsOfPolynom(polynom):
    listOfNumerators = []
    numerator = ''
    for i in range(len(polynom) - 2):
        if polynom[i] == 'x' and polynom[i - 1] == '+':
            listOfNumerators.append(1)
        if polynom[i] != 'x' and polynom[i] != '+' and polynom[i] != '=' and polynom[i] != ' ' and polynom[i] != '^':
            numerator += polynom[i]
        else:
            if numerator != '':
                listOfNumerators.append(int(numerator))
                numerator = ''
        if polynom[i] == 'x' and polynom[i + 2] == '+':
            listOfNumerators.append(1)
        if polynom[i - 2] != 'x' and polynom[i] == '=':
            listOfNumerators.append(0)
    resultList = []
    for j in range(1, len(listOfNumerators) + 1, 2):
        resultList.append((listOfNumerators[j - 1], listOfNumerators[j]))
        if j < len(listOfNumerators) - 2 and (listOfNumerators[j] != listOfNumerators[j + 2] + 1):
            resultList.append((0, listOfNumerators[j] - 1))
    return resultList


def sumPolinoms(polynom_1, polynom_2):
    numeratorsOfResultPolinom = []
    orderOfPolynom = max(polynom_1[0][1], polynom_2[0][1])
    if polynom_1[0][1] > polynom_2[0][1]:
        orderOfPolynom = polynom_1[0][1]
        for j in range(orderOfPolynom - polynom_2[0][1]):
            polynom_2.insert(0, (0, 0))
    elif polynom_1[0][1] < polynom_2[0][1]:
        orderOfPolynom = polynom_2[0][1]
        for j in range(orderOfPolynom - polynom_1[0][1]):
            polynom_1.insert(0, (0, 0))
    for i in range(orderOfPolynom + 1):
        numeratorsOfResultPolinom.append((polynom_1[i]
                                          [0] + polynom_2[i][0], orderOfPolynom - i))
    return numeratorsOfResultPolinom


def writePolynom(listOfNumeratorsOfPolynom: tuple):
    stringOfPolynom = ''
    keyForPlus = 0
    for i in range(len(listOfNumeratorsOfPolynom)):
        if listOfNumeratorsOfPolynom[i][0] != 0:
            if keyForPlus != 0:
                stringOfPolynom += '+ '

            if listOfNumeratorsOfPolynom[i][1] == 1 and listOfNumeratorsOfPolynom[i][0] == 1:
                stringOfPolynom += (f'x ')
            elif listOfNumeratorsOfPolynom[i][0] == 1:
                stringOfPolynom += (f'x^{listOfNumeratorsOfPolynom[i][1]} ')
            elif listOfNumeratorsOfPolynom[i][1] == 1:
                stringOfPolynom += (f'{listOfNumeratorsOfPolynom[i][0]}x ')
            elif listOfNumeratorsOfPolynom[i][1] == 0:
                stringOfPolynom += (f'{listOfNumeratorsOfPolynom[i][0]} ')
            else:
                stringOfPolynom += (
                    f'{listOfNumeratorsOfPolynom[i][0]}x^{listOfNumeratorsOfPolynom[i][1]} ')

            keyForPlus += 1

    stringOfPolynom += '= 0'
    return stringOfPolynom


def writeResultToFile(path, polynom):
    with open(path, 'w') as data:
        data.writelines(polynom)
    return 0


path_1 = Path('lesson_2', 'seminar_4', 'homework_4', 'file_1.txt')
path_2 = Path('lesson_2', 'seminar_4', 'homework_4', 'file_2.txt')
path_3 = Path('lesson_2', 'seminar_4', 'homework_4', 'file_3.txt')

print(writeResultToFile(path_3, writePolynom(sumPolinoms(getNumeratorsOfPolynom(readPolinom(path_1)),
                                                         getNumeratorsOfPolynom(readPolinom(path_2))))))
