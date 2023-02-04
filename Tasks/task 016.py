# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random 

def create_random_list(n):
    array = [random.randint(1,10) for i in range (n)]
    return array

n = int(input('Введите размер списка: '))
x = int(input("Введите искомое число: "))
array = create_random_list(n)


counter = 0
for i in range(0, len(array)):
    if array[i] == x:
        counter +=1
print(*array)
print(f'Число {x} встречается {counter} раз')
