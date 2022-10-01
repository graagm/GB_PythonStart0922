# HOMEWORK9 01.10.22
# Задача 1
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.


# def thesaurus(*args):
#     return {i: i for i in args}


# dc_final  = thesaurus("иван", "Мария", "Петр", "Илья", "Иван")

# print(dc_final)


# Задача 2
# Иван решил создать самый большой словарь в мире. 
# Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
#  состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# def biggest_dict(**kwargs):
#     my_dict = {'first_one': 'we can do it'}
#     for k, v in kwargs.items():
#         my_dict[k] = v
#     return my_dict

# print(biggest_dict(two='pleep'))


# Задача 4
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате 
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, 
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы. 
# Например: >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева") 
# { "А": { "П": ["Петр Алексеев"] }, "И": { "И": ["Илья Иванов"] }, "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } }

# def thesaurus_adv(*args):
#     dc = {}
#     for i in args:
#         if  i.split()[1][0].upper() in dc and i.split()[0][0].upper() in dc[i.split()[1][0].upper()]: 
#             dc[i.split()[1][0].upper()][i.split()[0][0].upper()].append(i)
#         else:
#             dc[i.split()[1][0].upper()] = dc.get(i.split()[1][0].upper(), {}) | {i.split()[0][0].upper() : [i]}            
#     return dc

# dc_final = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

# for k in sorted(dc_final):
#     print(f'{k} : {dc_final[k]}')
