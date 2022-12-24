# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def FilePolynomsImport(path):           # импорт полинома из файла
    with open(path) as polynom:
        poly = polynom.read()
    return poly


def PolynomToDictionary(poly):          # разбираем коэф.полинома на словарь

    poly_change = poly.replace('x ', 'x^1').replace(' ', '').replace('-', ' -').replace('+', ' ').replace('=0', '')
    poly_list = poly_change.split()
   
    poly_dict = {}

    for el in poly_list:
        if el.find('x') != -1:
            key = el[(el.find('x') + 2):len(el)]
            int_key = int(key)
            if el[0:el.find('x')] != '-':
                value = el[0:(el.find('x') - 1)]
            else:
                value = -1
            poly_dict[int_key] = value
            
        if el.find('x') == -1:
            int_key = 0
            value = el
            poly_dict[int_key] = value
    
    return(poly_dict)


def SumPolynoms(poly1, poly2):                  # складываем словари
    summ_polynom = {}
    for i in poly1:
        for k in poly2:
            summ_polynom[i] = int(poly2.get(i, 0)) + int(poly1.get(i, 0))
    for k in poly2:
        if k not in summ_polynom:
            summ_polynom[k] = int(poly2.get(k, 0))
    return summ_polynom
            

def DictionaryToPolynom(dic_polinom):           # словарь в полином
    sum_poly = ' '
    for el in dic_polinom:
        if el != 0:
            sum_poly += ' + ' + str(dic_polinom[el]) + '*x^' + str(el)
        elif el == 1:
            sum_poly += ' + ' + str(dic_polinom[el]) + '*x' + str(el)
        elif el == 0:
            sum_poly += ' + ' + str(dic_polinom[el])
        
    sum_poly = sum_poly + ' = 0'
    return sum_poly

def FilePolynomsNew(poly):                  # запись суммарного полинома в файл
    with open('PolySum.txt', 'w') as data:
        data.write(poly)
    

polynom1 = FilePolynomsImport('Poly01.txt')
polynom2 = FilePolynomsImport('Poly02.txt')

print(f'Полином из первого файла: {polynom1}')
print(f'Полином из второго файла: {polynom2}')

polynom1_dictionary = PolynomToDictionary(polynom1)
polynom2_dictionary = PolynomToDictionary(polynom2)

sorted_summ_polynom = dict(sorted(SumPolynoms(polynom1_dictionary, polynom2_dictionary).items(), reverse = True))

final_polynom = DictionaryToPolynom(sorted_summ_polynom).replace('+ -', '- ').replace('^1 ', ' ').replace('  + ', '')

FilePolynomsNew(final_polynom)
print(f'Сумма двух многочленов (также записана в новый файл): {final_polynom}')
