print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count # создаем переменную чтобы в цикле ее уменьшать
members = [] # чистый лист
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name) # добавляем участников в список
    i = i - 1 
    # можно записать как i-=1

#Кто участвовал в соревнованиях(по алфавиту)
print('В соревнованиях участвовали: ', sorted(members))
# мы записали людей с конца, .reverse() разворот списка
members.reverse()
# нам нужно взять первые 3 места
result = members[:3]
result = 'Победители: {}. Поздравляем!'.format(result)
print(result)



