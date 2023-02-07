# Работа со словарями

# my_dict = {'Иванов':'Петр', 'Петров': 'Иван', (1, 2, 3 ,4): 'это числа', 
# True: True, 123: [234,345,456,567], None: 'я не пустое место!', 
# 2: [1,2, [10, 20, [100, 200]]]}
# print(my_dict)

# my_dict['Иванов'] = 'Вася'
# print(my_dict)
# my_dict['Иванов'] += '-Вася'
# print(my_dict)

# my_dict['Сидоров'] = my_dict.pop('Петров')
# print(my_dict)

# print(my_dict.get(1234, 0))
# print(my_dict[123][2])
# print(my_dict[2][-1][2][0])

# Задача 25
# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# s = (input('Введите символы: '))
# s = s.split()
# print(s)
# result_dic = {} #dictionary в который будем класть счетчики какой символ сколько раз встречается
# new_s = [] # новый лист в который будем класть по условию в задаче
# for i in s:
#   if i not in result_dic:  # если еще нет в словаре, первый раз
#     new_s.append(i) # кладем наш символ
#     # print(i)
#     result_dic[i] = result_dic.get(i, 0)+ 1 # с помощью метода get возвращаем в словарь наш символ искусственно добавляя 1
#   else:  # если уже есть в словаре, значит пошли повторы
#     new_s.append(f'{i}_{result_dic[i]}') # кладем значение с постфиксом и значение из словаря
#     # print(f'{i}_{result[i]}')
#     result_dic[i] = result_dic.get(i, 0) + 1
# print(*new_s)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# new_text=text.lower()

# print(len(set(text.split())))
# print(len(set(new_text.split())))

# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# text = """She sells sea shells on the sea shore;The shells
# # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore,I'm sure that the shells are sea
# # shore shells."""
# new_text2 = text.lower().replace(";",' ').replace(",",' ')

# print(len(set(text.split())))
# print(len(set(new_text2.split())))

# text = input().split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих 
# слайдах

# Ваня:
# n = int(input())
# max_number = 1000 # - должно быть n
# while n != 0:
#     n = int(input())
#     if max_number > n: # n > max_number
#         max_number = n
# print(max_number)

# Петя:
# n = int(input()) 
# max_number = -1 # должно быть n
# while n < 0: # не правильный выхож
#     n = int(input())
#     if max_number < n:
#         n = max_number # ошибка max_number = n
# print(n) # ошибка



