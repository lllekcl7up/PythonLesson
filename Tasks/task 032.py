# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from notes import create_random_list
# Тут импортирую функцию из файла notes.py увидел на семинаре , решил попробовать. 

def finder_range_index(rand_list):
    lst = []
    for i in range(len(rand_list)):
        if rand_list[i] >= minimum and rand_list[i] <= maximum:
            lst.append(i)
    return lst


n = int(input('Введите размер списка: '))
minimum = int(input('Введите минимальный диапазон: '))
maximum = int(input('Введите максимальный диапазон: '))
rand_list = (create_random_list(n))

print(f'Массив {rand_list}')
print(f'Индексы {finder_range_index(rand_list)} элементов массваа в диапазоне от {minimum} до {maximum}')




