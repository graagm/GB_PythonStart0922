# HOMEWORK10 02.10.22
# Задача1

# import random

# ls1 = (random.randint(1,10) for _ in range(random.randint(7,15)))
# ls2 = (random.randint(1,10) for _ in range(random.randint(7,15)))

# print(*set(ls1).intersection(set(ls2)), sep=', ')

# Задача2

# from posixpath import split


# ls = input().split()
# set_app = set()
# for i in ls:
#     if i in set_app:
#         print('Yes')
#     else:
#         set_app.add(i)
#         print('No')


# Задача3
# import sys

# ls = list(k for j in (map(lambda s: s.strip(' ').lower(), i.strip(' \n').split()) for i in sys.stdin) for k in j)

# print(len(set(ls)))