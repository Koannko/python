# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Реализовано для вещественных чисел с дробной частью, состоящей не более, чем из 10 цифр
import math


def difMaxAndMinFractionalParts(listOfFloats):
    fractionalParts = []
    for num in listOfFloats:
        fractionalParts.append(round(math.modf(num)[0], 10))
    return max(fractionalParts) - min(fractionalParts)


print(difMaxAndMinFractionalParts([1.1, 1.4, 1.01]))  # => 0.39
print(difMaxAndMinFractionalParts([1.1, 1.2, 3.1, 1.01]))  # => 0.19
