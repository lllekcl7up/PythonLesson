#Вносим данные в файл
# with open('PythonLesson/Lesson 01/file.txt', 'a') as data:
#     data.write('line 2qw1\n')
#     data.write('line 2eq3\n')

#Вносим данные в файл
# colors = ['red', 'green', 'blue']
# data = open('PythonLesson/Lesson 01/file.txt','a')
# # data.writelines(colors) #разделителей не будет
# data.write('LINE 1\n')
# data.write('LINE 2\n')
# data.close()

# Весь код который будет после Exit выполнятся не будет
# exit()

# Считываем из файла данные
# path = 'PythonLesson/Lesson 01/file.txt'
# data = open(path,'r')
# for line in data:
#     print(line)
# data.close()

# #Обращаемся к файлу hello.py и отрабатываем там скрипт
# import hello as h # преобразуем имы файла в переменную
# print(h.f(1))

# Умножает символ число
def new_string(symbol,count = 3):
    return symbol * count
print(new_string('!'))
