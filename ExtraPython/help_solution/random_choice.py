# создайте функцию, которая принимает список и возвращает из него случайный элемент.
from random import choice
# numbers = [1,2,3,4,5,6,7,8,9,10]
def random_elem(numbers):
    return choice(numbers)

if __name__ =='__main__':
    print(random_elem([1,2,33,4,56,7,8,9,0]))