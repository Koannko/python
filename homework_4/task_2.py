# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def listOfNonRepeatNums(listOfNums):
    listOfNonRepeat = []
    for i in listOfNums:
        if listOfNums[i] not in listOfNonRepeat:
            listOfNonRepeat.append(i)
    return listOfNonRepeat


print(listOfNonRepeatNums([1, 2, 3, 3, 4, 5, 3]))  # -> [1, 2, 3, 4, 5]
