# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values

# trasformation = lambda x: x
# values = [1, 23, 42, ]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print("ok")
# else:
#  print("fail")
# /
# print(values)
# print(transformed_values)


# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def max_square_orbits(list1):
#     res = []
#     max1 = pi*list1[0][0]*list1[0][1]
#     max_a_b = (list1[0][0], list1[0][1])
#     for i in orbits:
#         mult = pi 
#         if pi * i[0]*i[1] > max1 and i[0] !=i[1]:
#             max1 = pi * i[0] *i[1]
#             max_a_b = (i[0], i[1])
#     return max_a_b

# max_lambda= lambda a , b: pi * a * b
# print(max_square_orbits(orbits))

# # Решение Владимира:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# one_lst, two_lst = zip(*orbits)
# my_list = []
# for i in range(len(one_lst)):        
#         if one_lst[i]== two_lst[i]:
#             my_list.append(0)
#         else: 
#             s = one_lst[i]* two_lst[i]
#             my_list.append(s)
            
# for i in range(len(one_lst)): 
#     if my_list[i] == max(my_list):
#         print(orbits[i])
        
# max_elem = max(my_list)
# i_max_elem = my_list.index(max_elem)
# print(orbits[i_max_elem])

# Решение от Лёхи
# from math import pi
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# orbits = [i for i in orbits if i[0] != i[1]]
# max_square = max([pi * i[0] * i[1] for i in orbits])
# max_square_a_b = [i for i in orbits if pi * i[0] * i[1] == max_square]
# print(max_square_a_b)

# Решение через лямда и фильтер
# from math import pi
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# maximum = max(list(map(lambda x:pi*x[0]*x[1] ,(filter(lambda i: i[0]!=i[1], orbits)))))
# far = filter(lambda y:pi*y[0]*y[1] == maximum, orbits)
# print(*list(far))


# Решение с Редьюс
# from functools import reduce
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# elliptic_orbits = [orbit for orbit in orbits if orbit[0] != orbit[1]]
# elliptic_orbits = list(filter(lambda x: x[0] != x[1], orbits))
# print(reduce(lambda x, y: x if x[0] * x[1] > y[0] * y[1] else y, elliptic_orbits))

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.

values = [0, 2, 10, 6] 


def same_by(characteristic, objects):
    objects1 = map(characteristic,objects)
    if objects1 == objects:
        




if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')





вот наша функция def same_by(characteristic, objects):
    for i in objects:
        if not characteristic(i):
            return False
    return True





