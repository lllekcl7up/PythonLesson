from random import randint 

def create_random_list(n):
    array = [randint(0,10) for i in range (n)]
    return array