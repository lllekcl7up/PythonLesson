# Дана строка текста. Напишите программу для подсчета
# стоимости строки, исходя из того, что один любой символ
# (в том числе пробел) стоит 60 копеек.
# Ответ дайте в рублях и копейках в соответствии с примерами.

# Решение
# text = input('Введите текст: ')
# rubles = len(text) * 0.6
# penny = len(text) * 60 % 100
# print(int(rubles),'p.',penny,'коп. ')

# Дана строка, состоящая из слов, разделенных пробелами.
# Напишите программу, которая подсчитывает
# количество слов в этой строке.

# text = input('Введите текст:').split()
# print(len(text))

# Китайский гороскоп назначает животным годы в 1212-летнем
# цикле. Один 1212-летний цикл показан в таблице ниже.
# Таким образом, 20122012 год будет очередным годом дракона.
# Напишите программу, которая считывает год и отображает
# название связанного с ним животного. Ваша программа должна
# корректно работать с любым годом, не только теми,
# что перечислены в таблице.

# z = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
# year = int(input())
# print(z[year % 12-8])

# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит
# порядок его последних пяти цифр на обратный.

# num = (input("Введите число 5ти или 6ти значное : "))
# lst1 = num[0:-5]
# lst2 = num[:-6:-1]
# lts3 = int(lst1+ lst2)
# print (lts3)

# На вход программе подаётся натуральное число.
# Напишите программу, которая вставляет в заданное число
# запятые в соответствии со стандартным американским
# соглашением о запятых в больших числах.

# num = int(input())
# print(f'{num:,}')

# n человек, пронумерованных числами от 11 до n, стоят в
# кругу. Они начинают считаться, каждый k-й по
# счету человек выбывает из круга, после чего счет
# продолжается со следующего за ним человека.
# Напишите программу, определяющую номер
# человека, который останется в кругу последним.
# решение не понятное ...
# n = int(input())
# k = int(input())

# res = 0
# for i in range(1, n+1):
#     res = (res + k) % i
# print(res + 1)

# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек,
# лежащих в каждой координатной четверти.

# number = int(input())
# first, second, third, fourth = 0, 0, 0, 0

# for _ in range(number):
#     x, y = map(int, input().split())
#     first += x > 0 and y > 0
#     second += x < 0 and y > 0
#     third += x < 0 and y < 0
#     fourth += x > 0 and y < 0

# print(f"Первая четверть: {first}")
# print(f"Вторая четверть: {second}")
# print(f"Третья четверть: {third}")
# print(f"Четвертая четверть: {fourth}")

# На вход программе подается строка текста из натуральных
# чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел,
# которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом.

# from random import randint

# num = [randint(1, 10) for i in range(5)] #str(input('Введите числа').split())
# print(num)
# count=0
# for i in range (1,len(num)):
#     if num[i]>num[i-1]:
#         count+=1
# print(count)

# Решение интернета
# numbers = [int(n) for n in input().split()]
# counter = 0

# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         counter += 1
# print(counter)

# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу, которая меняет
# местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов, то последний остается на своем месте.
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.

# from random import randint

# num = [randint(1, 10) for i in range(5)]
# print(num)

# for i in range(1,len(num)-1,2):
#     num[i], num[i + 1] = num[i + 1], num[i]
# print (num)

# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется
# список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний
# элемент становится первым,а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

# from random import randint

# num = [randint(1, 10) for i in range(5)]
# print(num)
# num.insert(0, num[-1])
# del num[-1]
# print(num)

# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела,
# расположенные по неубыванию.
# Формат выходных данных
# Программа должна вывести одно число – количество различных элементов списка.
# Примечание. Задачу можно решить без множеств.

# from random import randint

# num = [randint(1, 5) for i in range(10)]
# print(num)
# print(sorted(num))
# print(set(num))
# print(len(set(num)))

# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить
# честный жребий и определить, кто будет делать очередной модуль нового курса.
# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
# На первой строке записан выбор Тимура, на второй – выбор Руслана.
# Формат выходных данных
# Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур,
# Руслан или же они сыграют вничью.


# tim = input('выбор тимура? : ')
# rus = input('камень ножницы бумага')

# if tim == rus : print("Ничья")
# elif tim == "камень" and rus == "ножницы":
#     print("tim win")
# elif tim == "бумага" and rus == "камень":
#     print("tim win")
# elif tim == "ножницы" and rus == "бумага":
#     print("tim win")
# else:
#     print("rus win")

# timur = input()
# ruslan = input()
# result = {'камень': ['ножницы', 'ящерица'],
#           'ножницы': ['бумага', 'ящерица'],
#           'бумага': ['камень', 'Спок'],
#           'Спок': ['ножницы', 'камень'],
#           'ящерица': ['бумага', 'Спок']}
# if timur == ruslan:
#     print('ничья')
# else:
#     if ruslan in result[timur]:
#         print('Тимур')
#     else:
#         print('Руслан')

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 00.

# def string_to_list(txt):
#     lst = []  # объявляем пустой список
#     for x in txt:  # идем по строке
#         lst.append(x)  # добавляем буквы в список
#     print(lst)
#     return(lst)  # >>>> ['м', 'а', 'й']

# def counter_letters(lst):
#     counter = 0
#     for item in lst:
#         if item == 'p':
#             counter+=1
#     return (counter)

# # text = input('Введите О или Р: ')
# text = 'OPOPOPPPOOPO'
# txt = text.lower()
# lst = string_to_list(txt)
# print(txt)
# print(counter_letters(lst))

stroka = input().split('О')
res = max(stroka, key=len)
print(len(res))
