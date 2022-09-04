# Задача1

# s = input()
# sm = 0
# ls = (i for i in s if i.isdigit())
# print(sum(int(i) for i in ls))


# Задача2

# def fct(x):
#     if x == 0:
#         return 1
#     return x * fct(x-1)

# n  = int(input())

# ls = [fct(i) for i in range(1, n+1)]

# print(ls)


# Задача3

# n  = int(input())
# dc = ((1 * 1 / i) ** i for i in range(1, n+1))
# print(sum(i for i in dc))





# Задача4
# from random import randint

# from itertools import cycle

# ml = 1

# file = open('file.txt', 'r', encoding='UTF-8')

# n  = int(input())

# ls = [randint(-n, n) for _ in range(n+1)]

# listt = cycle(ls)

# for i in file:
#     try:
#         ml *= int(i[next(listt)])
#     except:
#         continue


# print(ml)
# file.close()


# Задача5

# from random import shuffle, randint

# n  = int(input())

# ls = [randint(-n, n) for _ in range(n+1)]
# shuffle(ls)
# print(ls)
