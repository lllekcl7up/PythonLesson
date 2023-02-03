# my_list = [2,3,5,7,4,3,5,3,2,45,6,3,12,5,7,4,5]
# new_set = set(my_list)
# new_list = list(set(my_list))
# new_tuple = tuple(set(my_list))
# cur_tuple = new_tuple[:-3]
# new_tuple = cur_tuple

# Вывод разный 
# print(*my_list)
# print(*my_list, sep=' ', end='\n')
# print(*my_list, sep='~~~', end='- теперь другой массив -')
# print(new_set)
# print(*my_list, sep='\n')


# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# my_list = [1,1,2,0,-1,3,4,4]
# s = set()
# my_list =list(set(my_list))
# print(len(my_list))

# my_list = [1,1,2,0,-1,3,4,4]
# print(len(set(my_list())))

# Задача 17
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число. 
# Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3] 
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# import random

# def create_random_list(total, min, max):
#     if total<0: total = -total
#     if min>max: min,max = max,min
#     array = [random.randint(min,max) for i in range (total)]
#     return array

# def array_shift (a):
#     print(f'Созданный список: {a}')
#     shift = int(input('Размер сдвига: '))
#     a = a[shift:] + a[:shift]
#     print(f'Сдвинутый список: {a}')

# n = int(input('Введите размер списка: '))
# bound1 = int(input('Введите первую границу: '))
# bound2 = int(input('Введите вторую границу: '))

# array = create_random_list(n,bound1,bound2)
# array_shift (array)

# Неработает
# your_list = [int(input('type element: ')) for i in range(int(input('type amount')))]
# k = int(input('type K: ')) % len(your_list)
# print(your_list)
# k_list = your_list[k:] + your_list[:k]





# Задача №21
# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# def dict_finder(d):
#     s = set()
#     for i in d:
#         for j in i:
#             if not i[j] in s:
#                 s.add(i[j])
#     print (s)

# dict_list = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# dict_finder(dict_list)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# import random

# def create_random_list(total, min, max):
#     if total<0: total = -total
#     if min>max: min,max = max,min
#     array = [random.randint(min,max) for i in range (total)]
#     return array

# array = create_random_list(5,0,10)
# print(array)

# counter = 0
# a = []
# for i in range(1,len(array)):
#     if array[i] > array[i-1]:
#         counter +=1
#         a.append(f'{array[i-1]} < {array[i]}')
# print(counter,a)
# print(a)

from random import randint 

my_list = [randint(-10,10) for _ in range(randint(1,10))]
print(my_list)

# counter=0
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i-1]:
#         counter +=1

# print(counter)


# Решение 2
from random import randint 

my_list = [randint(-10,10) for _ in range(randint(1,10))]
print(my_list)

new_list = [f'{my_list[i]} > {my_list[i-1]}' for i in range(1,len(my_list)) if my_list[i] > my_list[i-1]]
print(*new_list)
print(len(new_list))