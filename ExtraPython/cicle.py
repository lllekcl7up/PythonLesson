# повторяет , пока условие не выполниться ! 
while True: 
    number = int(input('Введите число: '))
    if number > 0 and number < 10:
        print(f'{number} в степени 2 = {number**2}')
        break
    else:
        print('Число должно быть больше 0 и меньше 10')