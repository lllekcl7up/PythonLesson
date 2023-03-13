# Практическое задание
# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например: 
# второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет: [5, 8]


my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
# set1 = set(my_list_1) 
# set2 = set(my_list_2)
# print(set1 - set2 )
# Решение от ГБ
# result = set(my_list_1) - set(my_list_2)
# print(list(result))
# тут мы получаем не верный результат 
# for number in my_list_1:
#     if number in my_list_2:
#         my_list_1.remove(number)
# print(my_list_1)
# Верное решение
for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)

date = '02.11.2013'
d,m,y = date.split('.')
print(d,m,y)
months = {
    '01':'Января',
    '11':'Ноября'
}
days = {
    '01': 'Первое',
    '02': 'Второе'
}
result = f'{days[d]} {months[m]} {y} года'
print(result)

my_list_3 = [2, 2, 5, 12, 8, 2, 12]
#     for item in my_list_3:
#     if my_list_3[i] == my_list_3[]
# print(set(my_list_3))
res = []
for number in my_list_3:
    if my_list_3.count(number) == 1: # тут мы смотрим какое число встречается только 1 раз.
        res.append(number)
print (res)


