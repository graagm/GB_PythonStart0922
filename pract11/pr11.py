# # Задача 1, график

# import math
# import sympy as sy 
# from sympy.plotting import plot as pl

# # Установим функцию для расчета значений по проходу по x
# def funcx(x):
#     return -12 * (x ** 4) * (math.sin(math.cos(x))) - 18 * (x ** 3) + 5 * (x ** 2) + 10 * x - 30

# # Зададим sympy для отрисовки графика
# x = sy.Symbol('x')
# f = -12 * (x ** 4) * (sy.sin(sy.cos(x))) - 18 * (x ** 3) + 5 * (x ** 2) + 10 * x - 30




# # Строим график, смотрим ориентиры точек
# pl(f)
# # Установим шаг
# diff_x = 0.001
# # Установим начало
# start_x = - 8
# # Установим конец
# end_x = 9
# step = start_x
# func_prev = funcx(step)
# step += diff_x
# func_step = funcx(step)
# step += diff_x
# func_next = funcx(step)
# # добавляем  список для локальных экстремумов
# ls_extrems = []
# while step < end_x:
#     if func_step < func_prev and func_step <  func_next:
#         print(f'Мы нашли локальный минимум Х={step - diff_x}, Y={func_step}')
#         ls_extrems.append([step - diff_x, func_step])
#         if len(ls_extrems) == 1:
#             print(f'Функция убывает от -оо  до  Х={step - diff_x}')
#         elif len(ls_extrems) > 1:
#             print(f'Функция убывает от {ls_extrems[-2][0]}  до  Х={ls_extrems[-1][0]}')
#     elif func_step > func_prev and func_step >  func_next:
#         print(f'Мы нашли локальный максимум Х={step - diff_x}, Y={func_step}')
#         ls_extrems.append([step - diff_x, func_step])
#         print(f'Функция возрастает от {ls_extrems[-2][0]}  до  Х={ls_extrems[-1][0]}')
#     func_prev = func_step
#     func_step = func_next
#     step += diff_x
#     func_next = funcx(step)

# print(f'Функция Возрастает от {ls_extrems[-1][0]}  до  +оо')

# print(f'вершина функции {sorted(ls_extrems, key=lambda x: x[1])[0]}')







# Задача 2,  Крестики-Нолики. Поле любого размера. Выигрыш при трех клетках с одинаоквым симовлом.

# class TicTacToeBoard():

#     def __init__(self, size = 3):
#         self.size = size
#         self.board = [['-' for _ in range(size)] for _ in range(size)]
#         self.count = 0
    
#     def new_game(self):
#         print(*self.board, sep='\n')
#         print(f'Игру начинает X, Пожалуйста, введите его координаты в игровом поле {self.size} x {self.size}')
    
#     def get_field(self):
#         print('Вы поймали игру в таком моменте:')
#         print(*self.board, sep='\n')

#     def check_field(self):
#         for i in range(self.size):
#             d_x= 0
#             d_o = 0
#             for j in range(self.size):
#                 if self.board[i][j] == 'X':
#                     d_o = 0
#                     d_x += 1
#                     if d_x == 3:
#                         return 'X'
#                 elif self.board[i][j] == 'O':
#                     d_x = 0
#                     d_o += 1
#                     if d_o == 3:
#                         return 'O'
#                 else:
#                     d_o = 0
#                     d_x = 0
#         for i in range(self.size):
#             d_x = 0
#             d_o = 0
#             for j in range(self.size):
#                 if self.board[j][i] == 'X':
#                     d_o = 0
#                     d_x += 1
#                     if d_x == 3:
#                         return 'X'
#                 elif self.board[j][i] == 'O':
#                     d_x = 0
#                     d_o += 1
#                     if d_o == 3:
#                         return 'O'
#                 else:
#                     d_o = 0
#                     d_x = 0
#         for i in range(self.size):
#             for j in range(self.size):
#                 if self.board[i][j] == 'X':
#                     try:
#                         chr_symb = self.board[i + 1][j +  1]
#                         if chr_symb == 'X':
#                             try:
#                                 chr_symb_2 = self.board[i + 2][j +  2]
#                                 if chr_symb_2 == 'X':
#                                     return 'X'
#                             except:
#                                 continue
#                     except:
#                         continue
#                 elif self.board[i][j] == 'O':
#                     try:
#                         chr_symb = self.board[i + 1][j +  1]
#                         if chr_symb == 'O':
#                             try:
#                                 chr_symb_2 = self.board[i + 2][j +  2]
#                                 if chr_symb_2 == 'O':
#                                     return 'O'
#                             except:
#                                 continue
#                     except:
#                         continue
#         for i in range(self.size):
#             for j in range(self.size):
#                 if self.board[i][j] == 'X':
#                     try:
#                         chr_symb = self.board[i - 1][j - 1]
#                         if chr_symb == 'X':
#                             try:
#                                 chr_symb_2 = self.board[i - 2][j -  2]
#                                 if chr_symb_2 == 'X':
#                                     return 'X'
#                             except:
#                                 continue
#                     except:
#                         continue
#                 elif self.board[i][j] == 'O':
#                     try:
#                         chr_symb = self.board[i - 1][j -  1]
#                         if chr_symb == 'O':
#                             try:
#                                 chr_symb_2 = self.board[i - 2][j -  2]
#                                 if chr_symb_2 == 'O':
#                                     return 'O'
#                             except:
#                                 continue
#                     except:
#                         continue
#         for i in range(self.size):
#             if '-' in self.board[i]:
#                 return None
#         return 'D'

#     def make_move(self, row, col):
#         if self.board[row][col] == '-':
#             if self.count % 2 == 0:
#                 self.board[row][col] = 'X'
#             else:
#                 self.board[row][col] = 'O'
#             self.count += 1
#             if self.check_field() is not None:
#                 print(f'{self.check_field()} - финал этой игры')
#         else:
#             print('Это поле занято')
#             self.get_field()




    

# game1 = TicTacToeBoard()
# game1.new_game()
# game1.make_move(0,0)
# game1.get_field()
# game1.make_move(0,1)
# game1.get_field()
# game1.make_move(1,1)
# game1.get_field()
# game1.make_move(0,2)
# game1.get_field()
# game1.make_move(2,2)
# game1.get_field()



# game1 = TicTacToeBoard(5)
# game1.new_game()
# game1.make_move(0,0)
# game1.get_field()
# game1.make_move(0,1)
# game1.get_field()
# game1.make_move(1,1)
# game1.get_field()
# game1.make_move(0,2)
# game1.get_field()
# game1.make_move(2,2)
# game1.get_field()