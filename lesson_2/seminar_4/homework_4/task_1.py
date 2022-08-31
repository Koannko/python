# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def primeMultiples(N):
    listOfPrimes = []
    for i in range(1, N + 1):
        if N % i == 0:
            listOfPrimes.append(i)
            N /= i
    return listOfPrimes


print(primeMultiples(123))
