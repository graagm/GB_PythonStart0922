# HOMEWORK
# Задача 1
# import random
#
# sm = 0
# sp = [random.randint(2, 10) for i in range(10)]
#
# print(sp)
#
# for i in range(0, len(sp), 2):
#     print(sp[i], end=' ')
#     sm += sp[i]
#
# print()
# print(sm)




# Задача 2
# import random
#
# sp = [random.randint(2, 10) for i in range(9)]
#
# print(sp)
#
# ls_sp = len(sp)
#
# for i in range(ls_sp // 2 + 1):
#     print(sp[i] * sp[ls_sp - i - 1])


# Задача 3
# import random
#
# sp = [round(random.random() * 20, 2) for i in range(10)]
#
# print(sp)
#
#
# mx_el = max(str(i).split('.')[1] for i in sp)
# mn_el = min(str(i).split('.')[1] for i in sp)
# print(mx_el)
# print(mn_el)
# print(int(mx_el) - int(mn_el))



# Задача 4

#
# n = int(input(), 10)
#
# print(bin(n)[2:])


# Задача 5

# fib_pol = [0, 1]
# fib_neg = [-1, 0]
#
#
# n = int(input())
# for i in range(n - 1):
#     last = len(fib_pol)
#     fib_pol.append(fib_pol[last - 1] + fib_pol[last - 2])
#     fib_neg.insert(0, -fib_neg[0] + fib_neg[1])
#
#
# fib_all = fib_neg[:-1] + fib_pol
# print(fib_all)



















# Practic
# Задача 1
# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import time
#
# n = time.time_ns()
#
# print(time.time_ns())
# print(str(n)[-3])



# Задача 2
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# sp = []
# for _ in range(7):
#     sp.append(input())
#
# print(sp)
#
# n = int(input())
#
# flag = False
# for i in sp:
#     if str(n) in i:
#         flag = True
#         print('Число есть в элементе списка')
#         break
# if not flag:
#     print('Числа в списке не оказалось')


# Задача 3
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# sp = []
# for _ in range(5):
#     sp.append(input())
#
# print(sp)
#
# s = input()
#
# count = 0
# idx = 0
# for i in range(len(sp)):
#     if s == sp[i]:
#         count += 1
#         if count == 2:
#             idx = i
#
# if idx:
#     print(idx)
# else:
#     print('Двух вхождений не нашлось')




