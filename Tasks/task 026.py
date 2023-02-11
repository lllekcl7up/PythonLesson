# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Без рекурсии
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# print (a**b)

# С рекурсией 
# def power(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * power(a, b - 1))

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print(f'{a} в степени {b} = {power(a, b)}')
