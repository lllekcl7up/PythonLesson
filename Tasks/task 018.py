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

# Решение Оксаны
# my_list = [int(input('type element: ')) for i in range(int(input('type amount: ')))]
# x = int(input('type X: '))
# if x in my_list:
#     print(x) # если х есть в изначальном списке то его и выводим
# else:
#     my_list.append(x) # добавили в первый список значение Х
#     my_list = sorted(my_list) # отсортировали список от меньшего к большему
#     if my_list.index(x) == len(my_list) - 1: # если искомый элемент самый большой
#         element2 = my_list[my_list.index(x) - 1] # ближайший слева элемент к искомому
#         print(element2)
#     elif my_list.index(x) == 0: # если искомый элемент самый маленький
#         element = my_list[my_list.index(x) + 1] # [1] ближайший справа элемент к искомому
#         print(element)
#     else: # если искомый элемент в середине, выводим оба соседних с ним элемнта
#         element = my_list[my_list.index(x) - 1] # ближайший слева элемент к искомому
#         print(element)
#         element2 = my_list[my_list.index(x) + 1] # ближайший справа элемент к искомому
#         print(element2)