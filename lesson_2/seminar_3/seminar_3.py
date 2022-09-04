# 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# Предположим, что длина случайного числа задается случайно и находится в диапазоне [1, 10].

# from time import perf_counter, perf_counter_ns

# def getRandomNum():
#     rand_num = perf_counter_ns()
#     length = ((int(str(rand_num)[12]) % 9) + 1) % 10
#     result = str(rand_num)[(length + 3) % 6:length + (length + 3) % 6:]
#     if int(result[0]) == 0:
#         return result[-1::-1]
#     return result

# 20. Определить, присутствует ли в заданном списке строк, некоторое число

# def isThereStr(num):
#     num = str(num)
#     str1 = ["sfkjfj123", "oopsvl312", "poi0845", "pjhsadj21"]
#     st1 = "".join(str1)
#     return bool(st1.rfind(num) + 1)


# print(isThereStr(321))

# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# def getNumOf2Entry(listOfStrings, whatFind):
#     counter = 0
#     for i in range(len(listOfStrings)):
#         if listOfStrings[i] == whatFind:
#             counter += 1
#             if counter == 2:
#                 return i
#     if counter < 2:
#         return -1


# print(getNumOf2Entry(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))

# # 22. Найти сумму чисел списка стоящих на нечетной позиции


# def sumOfNumsInOddPositions(listOfNums):
#     listOfNums = [1, 12, 43, 1, 0, 22, 13, 14, 15, 18]
#     result = 0
#     for i in range(len(listOfNums) // 2):
#         result += listOfNums[2 * i + 1]
#     return result

# 23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Написать программу преобразования десятичного числа в двоичное
# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел
# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
# Найти НОК двух чисел
# Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10
#       30*** , Подумать, что если точность вычисления до 1000 знаков после запятой
# Составить список простых множителей натурального числа N

# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя


# def row_of_nums(list_of_nums):
#     result_list = []
#     result_list.append(list_of_nums[0])
#     count = 0
#     for i in range(1, len(list_of_nums)):
#         if list_of_nums[i] > result_list[count]:
#             result_list.append(list_of_nums[i])
#             count += 1
#     return result_list


# print(row_of_nums([1, 5, 2, 3, 4, 6, 1, 7]))
# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# [1, 2, 3, 9, 10, 4, 5, 8, 4, 5, 6, 7]
# [1, 2, 3, 9, 10]
# [1, 2, 3, 4, 5, 8]
# [1, 2, 3, 4, 5, 6, 7]


def max_len_list(list_of_nums):
    result_list = []
    list_n = []
    count = 0
    # for u in range(len(list_of_nums)):
    #     list_n.append(list_of_nums[u])
    #     for v in range(u, len(list_of_nums) - 1):
    #         for k in range(1, len(list_of_nums) - 1):
    #             if list_n[count] == list_of_nums[v] - k:
    #                 list_n.append(list_of_nums[v])
    #                 count += 1
    #     result_list.append(list_n)
    #     list_n = []
    #     count = 0
    # for i in range(len(list_of_nums)):
    #     list_n.append(list_of_nums[i])
    #     for j in range(i, len(list_of_nums) - 1):
    #         if list_of_nums[j + 1] > list_n[count]:
    #             list_n.append(list_of_nums[j + 1])
    #             count += 1
    #     result_list.append(list_n)
    #     list_n = []
    #     count = 0

    for i in range(len(list_of_nums)):
        list_n.append(list_of_nums[i])
        for j in range(i, len(list_of_nums)):

            if list_n[count] == list_of_nums[j] - 1:
                list_n.append(list_of_nums[j])
                i = j
                count += 1
        result_list.append(list_n)
        list_n = []
        count = 0

    length = len(result_list[0])
    result_index = 0
    for n in range(1, len(result_list)):
        if length < len(result_list[n]):
            length = len(result_list[n])
            result_index = n
    return result_list


print(max_len_list([4, 3, 1, 2, 5, 3, 8]))
