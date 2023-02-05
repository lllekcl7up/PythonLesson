# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random 

def create_random_list(n):
    array = [random.randint(1,20) for i in range (n)]
    return array

def finder_near (array):
    num = array [0]
    for i in range(len(array)):
        if (abs(array[i]-x)<abs(num-x) or abs(array[i]-x)==abs(num-x) and array[i]<num):
            num=array[i]
    return num

n = int(input('Введите размер списка: '))
array = create_random_list(n)
# print(*array)
x = int(input("Введите искомое число: "))

near = finder_near(array)
print(f'Ближайшее по значению к числу {x} из списка {array} это {near}')

