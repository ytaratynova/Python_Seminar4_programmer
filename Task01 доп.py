#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральное число - степень многочлена: '))

koef = []
for i in range(k+1):
     koef.append(random.randint(-100, 100))
if koef[0] == 0:
     koef[0] == 1
print(f'Случайные коэффициенты: {koef}')

polynom_parts = []
for i in range(k):
    if koef[i] != 0:
        polynom_parts.append(koef[i])
        if (k-i) != 0:
            polynom_parts.append('*x')
            if (k-i) != 1:
                polynom_parts.append('^')
                polynom_parts.append(k-i)
    if koef[i+1] > 0: 
        polynom_parts.append('+')
if koef[k] != 0:
    polynom_parts.append(koef[k]) 
polynom_parts.append(' = 0')

polynom_string = ''.join(str(_) for _ in polynom_parts)
print(polynom_string.replace('+', ' + ').replace('-', ' - '))
