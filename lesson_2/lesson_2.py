# Файлы
# хранение данных, передача данных, хранение конфигов, логирование действий
# Происходит в текстовом формате (markdown), json, xml, все это текстовые файлы
# Режимы работы:
# а - открытие для добавления данных, дописывание
# r - открытие для чтения
# w - открытие для записи данных
# миксованные модификаторы: +w, +r
# # есть такая конструкция для дописывания данных:
# colors = ['r', 'g', 'b']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLINE\n')
# data.close()
# # а есть такой способ, когда не нужно руками закрывать файл
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2222\n')
# Чтобы прочитать файл:
path = 'file.txt'
# # path означает путь к файлу
data = open(path, 'r')
for line in data:
    print(line)
data.close()
# для импорта функции из другого файла:
# 1. import hello
# print(hello.f(1))
# 2. import hello as h
# print(h.f(1))


# Функции
# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string('!'))  # !!!
# print(new_string('!', 5))  # !!!!!

# чтобы передать сразу несколько аргументов в функцию:

# def concatenation(*params):
#     res: str = ''  # указание типа строка для переменной res
#     for item in params:
#         res += item
#     return res
# print(concatenation('a', 'b', 'c'))

# def sumOfNums(*num):
#     sum: int = 0
#     for x in num:
#         sum += x
#     return sum
# print(sumOfNums(2, 4, 5))

# Pекурсия. Числа фибоначи
# def fibonachi(N):
#     if N in [1, 2]:
#         return 1
#     else:
#         return fibonachi(N - 1) + fibonachi(N - 2)
# print(fibonachi(15))


# Кортежи - неизменяемые списки
# a = (2, 4)
# print(a[-1])
# создать кортеж из одного элемента:
# b = (3,)
# перебирать кортеж можно с помощью циклов
# конвертация списка в кортеж:
# t = tuple(['red', 'green', 'blue'])  # перевести
# print(t)
# r, g, b = t  # распаковка кортежа в отдельные переменные
# print('r: {} g: {} b: {}'.format(r, g, b))
# print(t)


# # Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#         '1': '!',
#         '2': '@',
#         '3': '#'
#     }
# print(dictionary)
# print(dictionary['1'])
# # получить все ключи:
# for k in dictionary.keys():
#     print(k)
# # получить все значения
# for v in dictionary.values():
#     print(v)
# # можно присвоить новое значение ключу


# # Множество - неупорядоченный набор данных
# colors = {'red', 'green', 'blue'}
# # если уже существует такой элемент, то множество не изменится
# colors.add('red')
# colors.remove('green')  # если такого элемента не существует, то будет ошибка
# # если такого элемента не существует, то ошибки не будет
# colors.discard('green')
# print(colors)
# print(type(colors))  # вернет set - это тип множество
# colors.clear()  # { }
# # логические операции над множеством
# a = {1, 2, 3, 4, 5}
# b = {2, 4, 7}
# c = a.copy()  # полное копирование
# u = a.union(b)  # объединение
# i = a.intersection(b)  # пересечение
# dl = a.difference(b)  # вычитание, есть в а, но нет в b
# dr = b.difference(a)  # есть в b, но нет в а
# # неизменяемое (замороженное) множество
# s = frozenset(a)


# Список list
# нельзя просто так копировать данные, получаются ссылки. Изменяя один список, меняется и другой
# list1 = [1, 2, 3, 4, 5]
# list1.pop()  # извлекает последний элемент из списка (удаляет)
# list1.pop(2)
# list1.append(13)
# list1.insert(2, 11)  # вставить на втору позицию число 11
# print(list1)
