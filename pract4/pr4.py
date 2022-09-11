# Homework 11.09.22
# Задача 1
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import random
#
# prex = len(input().split('.')[1])
# n = random.random() * 4000
# hec = len(str(n).split('.')[0])
# print(str(n)[:hec + prex + 1])


# Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# import sympy as sp
# print(*sp.primefactors(int(input())), sep=' ')



# Задача 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# import sys
#
# print(*set(int(i.strip('\n'))for i in sys.stdin), sep=', ')



# Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# s2 = ' + '.join(filter(lambda k: k[0] != '0', list(str(random.randint(0, 9)) + 'x^'f'{str(i)}' for i in range(2, int(input()) + 1))[::-1])) + ' + ' + \
#      (str(random.randint(1, 9)) + 'x') + ' + ' + str(random.randint(1, 9)) + '  = 0'

# file4 = open('task4.txt', 'w', encoding='UTF-8')
# print(s2, file=file4)
# file4.close()



# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# file1 = open('text1.txt', 'r', encoding='UTF-8')
# file2 = open('text2.txt', 'r', encoding='UTF-8')
# ls1 = file1.readline().split(' + ')
# ls2 = file2.readline().split(' + ')
# ls_sum = []

# print(ls1)
# print(ls2)

# ln_ms = len(ls1)
# for i in range(ln_ms - 1):
#     temp = ''
#     temp = str(int(ls1[i].split('*')[0]) + int(ls2[i].split('*')[0])) + ls1[i].split('*')[1]
#     ls_sum.append(temp)

# ls_sum.append(str(int(ls1[-1]) + int(ls2[-1])))

# print('+'.join(ls_sum))

# file1.close()
# file2.close()




                #МОДУЛЬ ПРАКТИКА с СЕМИНАРА


# Practic 11.09.22
# 1. Задайте строку из набора чисел.Напишите программу, которая покажет большее и меньшее число.В качестве символа - разделителя используйте пробел.
# Задача 1
# import random
# ls = list(map(int, input().split()))
#
#
# mx, mn = max(ls), min(ls)
#
# print(mx, mn, sep=' ')



# Задача 2
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
# вариант с sympy

        # import sympy as sp
        #
        # # a, b, c, x = sp.symbols('a b c x')
        # #
        # # print(sp.solve(a*x**2 + b*x + c, x))
        #
        # x = sp.Symbol('x')
        # a, b, c = int(input()), int(input()), int(input())
        #
        # print(sp.solve(a*x**2 + b*x + c, x))


# свой алгебраический вариант:

            # a, b, c = int(input()), int(input()), int(input())
            #
            # discr = b ** 2 - (4 * a * c)
            # try:
            #     k = discr ** 0.5
            #     rez1 = ((- b + k) / (2 * a))
            #     rez2 = ((- b - k) / (2 * a))
            #     if k == 0:
            #         print(rez1)
            #     else:
            #         print(rez1, rez2)
            # except:
            #     print('корней нет')



# Задача 3
# 3. Задайте два числа.Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел.
# import sympy as sp
#
# n, m = int(input()), int(input())
#
# nok = sp.lcm(n, m)
#
# print(nok)



# Задача 4
#  Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#  в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }


# from itertools import groupby
#
# def thesaurus(*args):
#     ls = groupby(sorted(list(args), key=lambda n: n[0].upper()), key=lambda n: n[0].upper())
#     return {i[0]: list(i[1]) for i in ls}
#     dc = {}
#     for i in args:
#         dc[i[0].upper()] = dc.get(i[0].upper(), []) + [i]
#     return dc
#
# dc_final  = thesaurus("иван", "Мария", "Петр", "Илья", "Иван")
#
# print(dc_final)


