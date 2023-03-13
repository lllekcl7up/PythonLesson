# Задача 9
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N
#  (произведение всех чисел от 1 до N) 0! = 1 
#  Решить задачу используя цикл while
# Input:       5
# Output:    120

# n = int(input("Введите число"))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)


# Решение Лёхи
# n = int(input('Введите целое неотрицательное число: '))
# while n < 0:
#     print('Введены неверные данные')
#     n = int(input('Введите целое неотрицательное число: '))

# def factorial_number(number):
#     factorial = 1
#     # i = 1
#     # while  i <= n:
#     #     factorial*= i
#     #     i+=1 
#     for i in range(1,n+1):
#         factorial*= i
#     return factorial

# factorial_n = factorial_number(n)
# print(factorial_n)

# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите 
# число -1.
# Input:     5
# Output:  6

# a = int(input("Введите число А: "))
# fib1 = 0
# fib2 = 1
# # list = [0,1] list для вывода чисел на экран
# n = 2 
# while a > fib2:
#     # t = fib1
#     # fib1 = fib2 
#     # fib2 = t + fib2
#     fib1,fib2 = fib2,fib1 + fib2 # присвоение фиб1 фиб2 , а фиб2 присвоить фиб1+ фиб2
#     # list.append(fib2)
#     n+=1
# # print(list)
# print(f"Число {a} по счету {n}" if a == fib2 else f"Число {a} не является числом Фибоначчи" )



# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая длинная 
# оттепель. Оттепелью они называют период, в который среднесуточная 
# температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых 
# дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2



# import random

# n = int(input('Введите число: '))

# list1 = []
# count = []
# for i in range(n):
#     list1.append(random.randint(-30,30))
#     count.append(0)
# print(list1)

# index = 0

# for i in range(len(list1)):
#     if list1[i] > 0:
#         count[index]+=1
#     else:
#         index+=1
# # print(count)

# max = count[0]
# for i in range(len(count)):
#     if count[i] > max:
#         max = count[i]
# print(max)


# Решение Оксаны
# n = int(input('type N, where 1 <= N <= 100: '))
# sum_pos = 0
# sum_max = 0
# for i in range(1, n + 1):
#     temperature = int(input('type temperature where min value -50, max value 50: '))
#     # print(i)
#     if temperature > 0:
#         sum_pos += 1
        
#     else:
#         if sum_pos > sum_max:
#             sum_max = sum_pos
#         sum_pos = 0
# if sum_pos > sum_max:
#     sum_max = sum_pos
# print(f'дней оттепели подряд: {sum_max}')


# 15. 
# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать
# арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# import random

# number = int(input("Введите число: "))

# numb = random.randint(1, 9)
# print(numb, end=' ')
# minimum = numb
# maximum = numb

# for i in range(number-1):
#     numb = random.randint(1, 9)
#     print(numb, end=' ')
#     if numb > maximum:
#         maximum = numb
#     elif numb < minimum:
#         minimum = numb
# print(f'\n {minimum} {maximum}')


