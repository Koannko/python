# Напишите программу, которая будет преобразовывать десятичное число в двоичное

# 1. Можно воспользоваться встроенным методом bin() и перевести строку в число, срезав все, кроме "0b"
def fromDecimalToBinarySystem(num):
    return int(bin(num)[2::])


print(fromDecimalToBinarySystem(132))  # => 10000100

# 2. Можно перевести с помощью циклического деления на 2, остановка, когда делимое меньше 2
# def fromDecimalToBinarySystem(num):
#     num = 132
#     result = ''
#     while num > 0:
#         result = str(num % 2) + result
#         num //= 2
#     return result

# print(fromDecimalToBinarySystem(132))  # => 10000100
