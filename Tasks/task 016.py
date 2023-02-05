# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random 

def create_random_list(n):
    array = [random.randint(1,10) for i in range (n)]
    return array

def finder (array):
    counter = 0
    for i in range(0, len(array)):
        if array[i] == x:
           counter +=1
    return counter

n = int(input('Введите размер списка: '))
array = create_random_list(n)
# print(*array)
x = int(input("Введите искомое число: "))

counter = finder(array)
print(f'Число {x} в списке {array} встречается {counter} раз')
