# Лекция 1 

# n = 5 # можно менять значения и будет меняться тип
# print (type(n)) # тут мы можем посмотреть тип переменной 

# что бы закомментировать выделенную область
#  Cntrl + K следом # Cntrl + C
# что бы РАЗкомментировать выделенную область
#  Cntrl + K следом # Cntrl + U 

# Ввод и Вывод в данных 

# print('Введите а');
# a = input()  # что бы конвертировать в числовое значение a = int(input())
# print('Введите b');
# b = input()
# print(a, b)
# print('{} -- {}'.format(a, b))
# print(a, ' + ', b)
# print(f"{a} тут можно писать текст  {b} {n}")
# с = input('Введите С: ') # на той же строке ввод в консоли будет 

# Привод числа к цело-численному значению и присвоение типа 
# с = 5.89
# print(с)
# print (type(с))
# с = int(с)  
# print(с)
# print (type(с))

# с = 43.329
# с = str(с)  # создает строковый тип
# print(с)
# print (type(с))


# с = 56
# с = bool(с)  # создает булевское значение (true / false)
# print(с < 100) 
# print (type(с))

# ОКРУГЛЕНИЕ чисел .

# a = 5.456789
# b = 6.456789
#print (round(a,3))
# print(round(a * b , 5 )) # кол-во цифр после запятой 



# Сокращённые операции и операции присваивания

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5


# ОПЕРАТОРЫ СРАВНЕНИЯ 
# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2 # и то и то должно быть правдой тогда TRUE
# print(a) # Если хотя бы одно из утверждений не верно тогда FALSE

# a = 1 < 4 or 5 < 2 # одно ИЗ утверждений правда тогда TRUE
# print(a) # Только если оба утверждения не верно тогда FALSE

# a = 1 == 2 # Проверяет равенство 
# print(a)

# a = 1 != 2 # Проверяет НЕ равенство 
# print(a)

# a = "Дима" # Сравнивает строки 
# b = "Дима"
# print (a == b)

# a = 1 < 3 < 5 < 10 # Если все утверждения верны то TRUE
# print (a)          # Если хотя бы одно НЕ верно, то FALSE

