def print_book():
    phonebook = open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt','r',encoding='utf-8')
    print(phonebook.read())
    phonebook.close()

def add_record(data):
    phonebook = open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt','a',encoding='utf-8')
    phonebook.write(' '.join(data)+'\n')
    phonebook.close()

def find_record(name):
    phonebook = open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt','r', encoding='utf-8')
    list_of_found_record = list()
    for lines in phonebook:
        # print(lines)
        if name in lines.split():
            list_of_found_record.append(lines)
    phonebook.close()
    return list_of_found_record

def change_record(meaning,new_meaning):
    with open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt', 'r',encoding='utf-8') as phonebook:
        book = phonebook.read()
    with open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt', 'w',encoding='utf-8') as phonebook:
        book = book.replace(meaning,new_meaning)
        phonebook.write(book)
    return book


def delete_record(name):
    with open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt', 'r',encoding='utf-8') as phonebook:
        book = phonebook.readlines()
        phonebook.seek(0)
    with open('S:\WorkGit\PythonLesson\Tasks\Phonebook\phone_book.txt', 'w',encoding='utf-8') as phonebook:
        for line in book:
            if name not in line: 
                phonebook.write(line)
    print("Удалено")
