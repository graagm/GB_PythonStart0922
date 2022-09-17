# Homework 17.09.22
# Задача 1
# 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# import sys
# import re
#
# text = list(re.sub(r'\w*абв\w*', '', i) for i in sys.stdin)
# print(''.join(text))



# Задача 2
# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# import random
# share_bons = 2021
# start_count = share_bons % 28 - 1
# game_bons = share_bons
# first_step_player1 = start_count
# print(f'Первый игрок берет в начале игры {first_step_player1} кнф.')
# game_bons -= first_step_player1
# while game_bons // 28 > 1:
#     step_player2 = random.randint(1, 28)
#     game_bons -= step_player2
#     step_player1 = game_bons % 28 - 1
#     game_bons -= step_player1
#     print(f'Второй взял {step_player2} кнф.   Первый взял {step_player1} кнф. Осталось {game_bons } кнф. ')
# last_step_player2 = random.randint(1, 28)
# game_bons -= last_step_player2
# last_step_player1 = game_bons
# print(f'Второй взял {last_step_player2} кнф.   Первый взял {last_step_player1} кнф.  И кнф. не осталось')



# Задача 3
# 3 Создайте программу для игры в ""Крестики-нолики"".


# import pygame as py
# import sys
# import time

# py.init()


# FPS = 60
# W = 850
# H = 900


# #COLORS
# Red = [255, 0, 0]
# White = [255, 255, 255]
# Black = [0, 0, 0]
# Ivory = [255, 255, 240]

# clock = py.time.Clock()
# sc = py.display.set_mode((W, H))

# sc.fill('WHITE')

# x = W / 2
# y = H / 2

# py.display.set_caption("Крестики и Нолики")

# # На будущую заморочку обновления разными поверхностями
# sc1 = py.Surface((100, 100))
# sc1.fill(Ivory)
# sc2 = py.Surface((100, 100))
# sc2.fill(Ivory)
# sc3 = py.Surface((100, 100))
# sc3.fill(Ivory)
# sc4 = py.Surface((100, 100))
# sc4.fill(Ivory)
# sc5 = py.Surface((100, 100))
# sc5.fill(Ivory)
# sc6 = py.Surface((100, 100))
# sc6.fill(Ivory)
# sc7 = py.Surface((100, 100))
# sc7.fill(Ivory)
# sc8 = py.Surface((100, 100))
# sc8.fill(Ivory)
# sc9 = py.Surface((100, 100))
# sc9.fill(Ivory)

# sc.blit(sc1, (250, 250))
# sc.blit(sc2, (350, 250))
# sc.blit(sc3, (450, 250))
# sc.blit(sc4, (250, 350))
# sc.blit(sc5, (350, 350))
# sc.blit(sc6, (450, 350))
# sc.blit(sc7, (250, 450))
# sc.blit(sc8, (350, 450))
# sc.blit(sc9, (450, 450))

# # отрисовали сетку
# for k in range(4):
#     py.draw.line(sc, Black, (250, 250 + 100 * k), (550, 250 + 100 * k), 3)
# for k in range(4):
#     py.draw.line(sc, Black, (250 + 100 * k, 250), (250 + 100 * k, 550), 3)


# # играем только на игровом поле!
# def err_text(x, y):
#     font1 = py.font.SysFont('arial', 12)
#     text1 = font1.render('Ждем на игровом ПОЛЕ', True, Black)
#     textRect1 = text1.get_rect()
#     textRect1.center = (x, y)
#     sc.blit(text1, textRect1)
#     py.display.update()
#     time.sleep(2)
#     for _ in range(5):
#         text1 = font1.render('Ждем на игровом ПОЛЕ', True, White)
#         textRect1 = text1.get_rect()
#         textRect1.center = (x, y)
#         sc.blit(text1, textRect1)
#         py.display.update()
#     return

# # рисуем крестик
# def x_draw(x, y):
#     if x < 250 or x > 550 or y < 250 or y > 550:
#         err_text(x, y)
#         return
#     x = ((x - 250) // 100) * 100 + 250
#     y = ((y - 250) // 100) * 100 + 250
#     py.draw.line(sc, Red, [x, y], [x + 100, y + 100], 2)
#     py.draw.line(sc, Red, [x + 100, y], [x, y + 100], 2)
#     return


# # рисуем нолик
# def o_circl(x, y):
#     if x < 250 or x > 550 or y < 250 or y > 550:
#         err_text(x, y)
#         return
#     x = ((x - 250) // 100) * 100 + 250
#     y = ((y - 250) // 100) * 100 + 250
#     py.draw.circle(sc, Red, [x + 50, y + 50], 50, 2)
#     return

# # пошла игра. Игроки сами разберутся кто выиграл
# while 1:
#     for i in py.event.get():
#         if i.type == py.QUIT:
#             sys.exit()

#         clock.tick(FPS)

#         if i.type == py.MOUSEBUTTONDOWN:
#             pos = py.mouse.get_pos()
#             x_coor = pos[0]
#             y_coor = pos[1]
#             if i.button == 1:
#                 x_draw(x_coor, y_coor)
#             else:
#                 o_circl(x_coor, y_coor)

#     py.display.update()
#     py.time.delay(20)




# Задача 4
# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def code_string(s):
#     start_ch = s[0]
#     new_str = ''
#     count = 1
#     for i in range(1, len(s)):
#
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             new_str += s[i - 1] + str(count)
#             count = 1
#     return new_str + s[- 1] + str(count)
#
# print(code_string('aaaaaaaayyyyyyyyjgdgyyyyyyggggggg'))
#
#
# def encode_string(s):
#     new_str = ''
#     for i in range(0, len(s) - 1, 2):
#         new_str += s[i]*int(s[i + 1])
#     return new_str
#
# print(encode_string(code_string('aaaaaaaayyyyyyyyjgdgyyyyyyggggggg')))