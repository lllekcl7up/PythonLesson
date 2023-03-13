# =========================================================
#              Встроенные функции и функции def 
# =========================================================

# print, type, range, len, input, int , float, str..

# Тип переменной - функция с параметрами и возвращаемым значением
t = type(123)
print (type(t))
# Диапазон - функция с параметрами и возвращаемым значением 
r = range(10)
# длинна последовательности
print(len([1,2,3,4]))
# преобразование типов 
int ('10')
str(10)
# ...
# =========================================================
#              Полезные встроенные функции 
# =========================================================
"""
* abc - модуль числа 
* min,max - минимальное, максимальное значение
* round - округление числа
* sum - сумма элементов последовательности 
* enumerate - нумерация последовательности
"""
print(abs(-7))
numbers = [5,15,7,1,-9,0]
print(max(numbers))
print(min(numbers))
print(round(10.9872,2))
print(sum(numbers))
# enumerate
winners = ['Dima', 'Kate', 'Roma']
for number,winner in enumerate(winners,1):
    print(number,winner)
# =========================================================
#              Создание собственных функции 
# =========================================================
"""
* Простой разделитель - нет параметров нет возврата 
* Меняем знак разделителя - 1 параметр нет возврата 
* Меняем знак и длину - 2 параметра нет возврата 
* Как использовать разделитель в тексте вместо того чтобы печатать его
в консоль? 2 параметра и результат ( возвращаемое значение)
"""
def get_sep(sep,sep_len):
    # print(sep * sep_len)
    return (sep * sep_len)
# меняем знак разделителя
print(get_sep('-',100))
print(get_sep('*',100))
# меняем знак и длину разделителя
print(get_sep('*',50))
# Используем разделитель в тексте 
sep = get_sep('*',50)
text = 'Hello{}Func{}'.format(sep,sep)
print(text)
"""
        ПЕРЕДАЧА ПАРАМЕТРОВ 
* По порядку 
* greeting ('Dima','Hello')
* По имени
* greeting(say= 'Hello',who='Dima')
"""
def greeting(who,say):
    print(say,who)

greeting('Dima','Hello')
greeting(say= 'Hello',who='Dima')

"""
        Значения по умолчанию 
* Можно указать у параметра значение по умолчанию
* def greeting(who, say='Hello')
* Если мы не передадим параметр say при вызове greeting('Max')
* То функция сработает со значением по умолчанию.
"""
# ====================================================
"""
        args,kwargs
* Иногда нужно реализовать передачу любого количества аргументов:
* def greeting('Hello', 'Leo', 'Max', 'Kate', ...)
* args - передача любого количества по порядку
* kwargs - передача любого количества по имени
 """
def greeting1(say,*args):
    print(say,args) # тут получаем картеж
greeting1('Hello','Dima','Kate','Roma')

# Тут функция принимает сколько угодно параметров
def get_person(**kwargs): # тут получаем словарь , и по ключу можно к нему обращаться 
    for k,v in kwargs.items():
        print(k,v)
get_person(name='Dima',age=40,has_car=True,city='Korolev')
"""
        Функция - тоже объект
* можно записать в переменную.
* Её можно передавать параметром в другие функции.
        Применение
* возможность не только входных данных, но и входных функций
* внутри функции переменными являются
* алгоритм
* последовательность действий
* сами действия
 """
def my_filter(numbers,function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1,2,3,4,5,6,7,8]
# фильтрует только четные числа
def is_even(number):
    return number % 2 ==0
print(my_filter(numbers,is_even))
# фильтрует только нечетные числа
def is_not_even(number):
    return number % 2 !=0
print(my_filter(numbers,is_not_even))
# фильтрует только числа больше 4
def big_4(number):
    return number > 4
print(my_filter(numbers,big_4))
# =========================================================
#                   lambda-функции
# =========================================================
"""
* применяются для создания анонимных функций по месту их использования
* lambda входные параметры: результат
 """
# фильтрует только четные числа
print(my_filter(numbers,lambda number: number % 2 ==0))
# фильтрует только нечетные числа
print(my_filter(numbers,lambda number: number % 2 != 0))
# фильтрует только числа больше 4
print(my_filter(numbers,lambda number: number > 4))
# =========================================================
#                  sorted, filter, map
# =========================================================
"""
        sorted
* сортировка последовательности
* sorted(iterable, *, key=None, reverse=False)
* аргументы: последовательность, ключ для сортировки, порядок
 """
numbers = [1,5,3,5,9,7,11]
print(sorted(numbers))
print(sorted(numbers,reverse=True))
#набор строк
names = ['Dima','Kate','Roma','Anna','Ira']
# сортировка по алфавиту
print(sorted(names))
print(sorted(names,reverse=True))
# города и численность населения 
cities = [('Москва',1000),('Лас-Вегас',500),('Антверпен',2000)]
# Так сортировка будет только по алфавиту
print(sorted(cities))
# Создав новую функцию , в которой указываем параметр город , и просим
# сортировать кортеж не с первого элемента а со второго. тоесть с индексом 1
def by_count(city):
    return(city[1])
print(sorted(cities,key=by_count))
#с лямбдой сортировка по ключу и по указанному элементу 
print(sorted(cities,key=lambda city: city[1]))
"""
        filter
* фильтрация последовательности
* filter(function, iterable)
*аргументы: функция фильтрации, последовательность
 """
numbers = [1,2,3,4,5,6,7,8]
# фильтрует только четные числа
print(list(filter(lambda number: number % 2 ==0,numbers)))
#набор строк
names = ['Dima','Kate','Roma','Anna','Ira']
print(list(filter(lambda name: len(name)==3,names)))
"""
        map
* применение функции к каждому элементу последовательности
* map(func, iterable, ...)
* аргументы: функция, последовательность
 """
numbers = [5,3,4,7,8]
# получить список квадратов чисел
print(list(map(lambda x: x**2,numbers)))
# привести числа к строке
print(list(map(lambda x: str(x),numbers)))
