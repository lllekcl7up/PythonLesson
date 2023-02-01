# Задача 2: Найдите сумму цифр трехзначного числа. 

number = int(input("Введите число: "))
sum = 0
if number < 0: # Проверяем на отрицательность 
    number = number * - 1 # если да , то делаем положительным
while (number > 0):
        num = number % 10
        sum = sum + num
        number = number // 10
        # number //= 10 можно так записать
print("Сумма цифр равна: ", sum)

# Решение группы
# n = input('Введите трехзначное число: ')
# print(int(n[0])+int(n[1])+int(n[2]))



