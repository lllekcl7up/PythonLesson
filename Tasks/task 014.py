# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

number = int(input('Введите число: '))

def DegreeTwo(n):
    degree = []
    for i in range(n):
        k = 2**i
        if k <= n:
            degree.append(k)
    return degree

print(DegreeTwo(number))