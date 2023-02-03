# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint as rndm

def HeadsAndTails(list1):
    tails = 0
    heads = 0
    for i in range(len(list1)):
        if list1[i] == 1:
            heads +=1
        else:
            tails +=1
    if heads < tails:
        return heads
    else:
        return tails


number = int(input("Введите число монеток: "))
coins = []
for i in range(number):
    coins.append(rndm(0,1))
print(coins)
print(HeadsAndTails(coins))

