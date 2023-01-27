# Задача 2: Найдите сумму цифр трехзначного числа. 

number = int(input("Введите трёх значное число: "))
sum = 0
if number < 0:
    number = number * - 1
while (number > 0):
        num = number % 10
        sum = sum + num
        number = number // 10
print("Сумма цифр равна: ", sum)





