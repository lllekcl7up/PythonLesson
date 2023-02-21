# Задача No49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

#Модули: 
# ИМпорт данных в тхт
# экспорт данных в тхт
# внесение записи через консоль 
# изменение и удаление записи через консоль 
# поиск записи по любому вхождению 
# user interface

import os, sys

def main_import_contacts():
    phonebook = dict()
    with open(os.path.join(sys.path[0],'phonebook.txt'),'r' ) as data:
    # with open('D:\Geekbrains\PythonLesson\Lesson 01\21.02.2023\phonebook.txt','r', encoding='utf-8') as data:
        s =data.readline()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
        # print(phonebook)

def import_contacts(some_string):
    finded_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(phonebook[[i]])
    return finded_contacts

def export_contacts(new_line):
    with open(os.path.join(sys.path[0],'phonebook.txt'),'a+') as data:
    # with open('D:\Geekbrains\PythonLesson\Lesson 01\21.02.2023\phonebook.txt','a+',encoding='utf-8') as data:
        data.writelines(' '.join(new_line)+'\n')


def input_contact():
    new_contact = [input('surname: ')]
    new_contact.append(input('name: '))
    new_contact.append(input('given name: '))
    new_contact.append(input('phonenumber: '))
    print(new_contact)
    export_contacts(new_contact)





def find_contact():
    s  = import_contacts(input('what we search?: '))

def user_interface():
    print('Phonebook\nwhadda want?\n1 - add contact\n2 - find contact\nany other input - end program')
    user_input = input('your choise:' )
    while user_input in ('1','2','3'):
        if user_input == '1':
            input_contact()
        elif user_input == '2':
            find_contact()
        elif user_input == '3':
            print()
            for i in phonebook[i]:
                print(*phonebook[i])
        user_input = input('\nyour choise')

    print('bye')



user_interface()
phonebook = dict()
input_contact()












