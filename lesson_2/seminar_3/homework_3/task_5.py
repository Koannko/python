# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
def negaFibonacci(num):
    listOfNums = [1, -1]
    for i in range(2, num):
        print(listOfNums)
        listOfNums.append(listOfNums[i - 2] - listOfNums[i - 1])
    return listOfNums


print(negaFibonacci(30))
