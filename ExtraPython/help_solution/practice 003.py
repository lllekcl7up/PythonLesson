# Практическое задание
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
# ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2).
# #  Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# # ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
# # Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:

# 1.
# def person(name,age,city):
#     return name,age,city
# # person('Dima','39','Korolev')
# text = '"{}, {}лет, проживает в городе {}"'.format('Dima','39','Королев')
# print(text)
def person_info(name,age,city):
    result = f'{name}, {age} год(а) проживает в городе {city}'
    return result
print(person_info('Kate',33,'Moscow'))

def get_max(num1,num2,num3):
    return max(num1,num2,num3)
print(get_max(41,1,7))

#3 игра

player_name = input('Введите имя игрока')

player = {
    'name':player_name,
    'health':100,
    'damage':50,
    'armor':1.2
}
enemy_name = input('Введите имя врага')

enemy = {
    'name':enemy_name,
    'health':50,
    'damage':30,
    'armor':1
}

def get_damage(damage,armor):
    return damage/armor

def attack(unit,target):
    damage = get_damage(unit['damage'],target['armor'])
    target['health'] -= damage

attack(player,enemy)
print(enemy)

attack(enemy,player)
print(player)
