# Шаг 1. Загадать случайное число
import os
os.system('cls')
import random
number = random.randint(1,100)
# print(number)

# Шаг 2. Предложить пользователю ввести число
# print(user_number)

print("""
    ----------------------------------------------------
            ИГРА - УГАДАЙ ЧИСЛО - (от 1 до 100)
    ----------------------------------------------------
             Выберете уровень сложности:
             
    Нажмите '1' - 10 попыток (легко)
    Нажмите '2' - 5 попыток  (средне)
    Нажмите '3' - 3 попытки  (трудно)
    """)

user_number = None
count = 0 
levels = {1:10,2:5,3:3}
level = int(input('Введите уровень сложности: '))
max_count = levels[level]
user_count = int(input('Введите количество игроков: '))
users = []
is_winner = False
winner_name = None

for index in range(user_count):
    user_name = input(f'Введите имя {index+1} игрока: ')
    users.append(user_name)
print()
print('Здравствуйте игроки:')
print(*users)
print()
# Шаг 3. Сравнение чисел . Вывод результата
while not is_winner:
    count +=1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка №: {count}\n')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number > user_number:
            print('Число больше\n')
        else:
            print('Число меньше\n')
else:
    print(f'Победитель {winner_name} !!!')