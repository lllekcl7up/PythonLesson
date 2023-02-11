# Задача №31. Решение в группах 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1,
# ak = ak-1 + ak-2 (k > 1).Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def Fibonacci(n: int):
#     if n == 0:
#         return 0
#     if (n == 1 or n == 2):
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# n = int(input('Введите число Фибоначчи'))
# for  i in range(n):
#     num_fib = Fibonacci(i)
#     print(i+1, '-', num_fib)
# print(i+1, 'Число Фибоначчи -',num_fib)

# Решение разработчиков Python
# n = int(input())
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# estimates = [int(x) for x in input().split()]
# print(estimates)

# def min_replace_max(list1: list):
#     max1 = max(list1)
#     min1 = min(list1)
#     for i in list1:
#         if list1[i] == max1:
#             list1[i] = min1

# list1 = min_replace_max(estimates)
# print(list1)
# print(estimates)

# def vasya(marks_list):
#     max_value = max(marks_list)
#     min_value = min(marks_list)
#     for i in range(len(marks_list)):
#         if marks_list[i] == max_value:
#             marks_list[i] = min_value
#     print(marks_list)
# a = [1,3,3,3,5]
# print(a)
# vasya(a)

 
# from random import randint
# my_list = [randint(1,5) for _ in range(randint(3,7))]
# print(my_list)
# max_elem = max(my_list)
# min_elem = min(my_list)

# for i in range(len(my_list)):
#     if my_list[i] == max_elem:
#         my_list[i] = min_elem

# print(my_list)


# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def check(num):
#     for i in range (2, num//2 + 1):
#         if num % i == 0:
#             return 'No'
#     return 'Yes'
# num = int(input('Введите число: '))
# number = check(num)
# print(number)


# def simple_num(x):
#     num = list(range(2,x))
#     for i in num:
#         if x % i == 0:
#             return 'No'
#     return 'Yes'

# n = int(input('Введите число:  '))
# print(simple_num(n))




# # Задача №37. Дано натуральное число N и последовательность из N элементов.
# # Требуется вывести эту последовательность в обратном порядке.
# # Примечание.
# В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# # Input: 2 -> 3 4
# # Output: 4 3

# from random import randint

# n = 6

# def recurs(x):
#    if x == 0:
#         print()
#         return

#    number = randint(0,100)
#    print(number, end=" ")
#    recurs(x-1)
#    print(number, end=" ")

# recurs(n)