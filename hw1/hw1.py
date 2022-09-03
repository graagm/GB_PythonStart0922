# Задача6:
# day = input()
# if day in '67':
#     print('да')
# else:
#     print('нет')

# Задача7:
# x, y, z = range(0,2), range(0,2), range(0,2)
# for i in x:
#     for j in y:
#         for k in z:
#             print(i, j, k)
#             print((not any((i, j, k))) == all((not i, not j, not k)))



# Задача8:
# x, y = int(input()), int(input())
# if x == 0 :
#     print('Вы на оси y')
# elif y == 0:
#     print('Вы на оси x')
# elif x > 0 and y > 0:
#     print(f'Точка {x}, {y} в четверти 1')
# elif x < 0 and y > 0:
#     print(f'Точка {x}, {y} в четверти 2')
# elif x < 0 and y < 0:
#     print(f'Точка {x}, {y} в четверти 3')
# elif x > 0 and y < 0:
#     print(f'Точка ({x}, {y}) в четверти 4')



# Задача9:
# quarter = int(input())
# if quarter == 1:
#      print('В первой четверти  x>0, y>0')
# elif quarter == 2:
#      print('Во второй четверти  x<0, y>0')
# elif quarter == 3:
#      print('В третьей четверти  x<0, y<0')
# elif quarter == 4:
#      print('В четвертой четверти  x>0, y<0')
# else:
#      print('Вы в дургой плоскости')



# Задача10:
# x1, y1 = input().split()
# x2, y2 = input().split()
# s = ((int(x2)-int(x1)) ** 2 + (int(y2)-int(y1)) ** 2) ** 0.5
# print(round(s, 2))