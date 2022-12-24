# Рандомайзер
# Программа генерирует случайное число, используя функцию time и немного еe преобразив. 
# Количество цифр в числе - показывает последняя цифра, полученна в результате преобразования time.
# Само число - перевернутое, преобразовнное time с нужным количеством цифр.

import time

def RandomNumber():

    random_time_number = int(time.time() * 99999999 // 100)     # генерация случайного числа по функции времени
    
    if random_time_number % 10  != 0:                           # определение количества цифр в числе
         digit_quantity = random_time_number % 10 
    else:
        digit_quantity = 1            

    random_time_number = random_time_number // 10

    random_number = 0

    for i in range(1, digit_quantity + 1):                      # расчет случайного числа
        random_number = random_time_number % 10 * 10 ** (digit_quantity - i) + random_number
        random_time_number = random_time_number // 10

    return random_number

print(f'Ваше случайное число: {RandomNumber()}')





