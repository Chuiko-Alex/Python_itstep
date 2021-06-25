import random
"""
                  Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах.
"""


def task_1():
    cortege_1 = tuple(random.randint(0, 10) for i in range(10))
    cortege_2 = tuple(random.randint(0, 10) for i in range(10))
    cortege_3 = tuple(random.randint(0, 10) for i in range(10))
    dict_cortege = []
    for i in cortege_1:
        if i in cortege_2 and i in cortege_3:
            dict_cortege.append(i)
    return  set(dict_cortege)

print("Решение Задание 1:", task_1())



"""
                  Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка.
"""


def task_2():
    cortege_1 = tuple(random.randint(0, 10) for i in range(10))
    cortege_2 = tuple(random.randint(0, 10) for i in range(10))
    cortege_3 = tuple(random.randint(0, 10) for i in range(10))
    dict_cortege = []
    for i in cortege_1:
        if i not in cortege_2 and i not in cortege_3:
            dict_cortege.append(i)
    for i in cortege_2:
        if i not in cortege_1 and i not in cortege_3:
            dict_cortege.append(i)
    for i in cortege_3:
        if i not in cortege_1 and i not in cortege_2:
            dict_cortege.append(i)
    return set(dict_cortege)

print("Решение Задание 2:", task_2())



'''
                  Задание 3
Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции.
'''


def task_3():
    cortege_1 = tuple(random.randint(0, 3) for i in range(10))
    cortege_2 = tuple(random.randint(0, 3) for i in range(10))
    cortege_3 = tuple(random.randint(0, 3) for i in range(10))
    index = 0
    dict_cortege = []
    for i in cortege_1:
        if i == cortege_2[index] and i == cortege_3[index]:
            dict_cortege.append(i)
        index += 1
    return dict_cortege

print("Решение Задание 3:", task_3())



'''
                  Задание 4
Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.
'''


### Есть 4 действия на выбор (add, delete, search, replacement), пропишите одно из действий и следуйте дальнейшим
### указаниям
def task_4(act = input('Что вы хотите(add, delete, search, replacement)?: ')):
    dict_bassketball_players = {'Alexander Sizonenko':'245', 'Sun Mingming':'236', 'Ri Myung-hoon':'235'}
    print("Все игроки, которые есть сейчас в словаре: ", dict_bassketball_players)

### Реализовал функцию добавления нового баскетболиста и его рост в словарь, нужно ввести в
### инпутах его имя и рост, и оно добавит его в словарь
    if act == 'add':
        name = input('Введите ФИО баскетболиста: ')
        height = input('Введите рост баскетболиста: ')
        dict_bassketball_players[name] = height
        return dict_bassketball_players

### Реализовал функцию удаления баскетболиста для этого нужно ввести ФИО уже имеющегося баскетболиста в словаре
### и оно его удалит
    elif act == 'delete':
        name = input('Введите ФИО баскетболиста, что бы удалить его из словаря: ')
        del dict_bassketball_players[name]
        return dict_bassketball_players

### Реализовал функцию поиска баскетболиста для этого нужно ввести ФИО уже имеющегося баскетболиста в словаре
### и оно его его найдет в словаре если он есть, если его нет, оно напишет что его нет
    elif act == 'search':
        name = input('Введите ФИО баскетболиста, что бы найти его: ')
        if name in dict_bassketball_players:
            return f'{name}, Есть в словаре'
        else:
            return f'{name}, Нет в словаре'

### Реализовал функцию замены ФИО и роста имеющегося в словаре баскетболиста на выбор,
### Если вы хотите заменить ФИО, в первом инпуте пишите фразу ФИО потом пишете имя баскетболиста, которое хотите заменить
### и пишите на какое имя вы хотите заменить.
### Если вы хотите заменить Рост, в первом инпуте пишите фразу Рост потом пишите имя баскетболиста у которго нужно
### заменить рост и пишите новый его рост.
    elif act == 'replacement':
        name_or_height = input("Что вы хотите заменить (ФИО или Рост), выберите одно из действий: ")
        if name_or_height == 'ФИО':
            name = input('Введите старое ФИО баскетболиста, что бы заменить: ')
            new_name = input('Введите новое ФИО баскетболиста, что бы заменить: ')
            dict_bassketball_players[new_name] = dict_bassketball_players.pop(name)
            return dict_bassketball_players
        elif name_or_height == 'Рост':
            name = input('Введите старое ФИО баскетболиста, что бы заменить ему рост: ')
            height = input('Введите новый рост баскетболиста: ')
            dict_bassketball_players[name] = height
            return dict_bassketball_players
        else:
            print('Данного действия нет в списке, запустите программу заного и выбирите одно из действий(ФИО или Рост)')
    else:
        print('Вы выбрали то, что програма не умеет, пожалуйста запустите програму заного и выбирите одно из действий(add, delete, search, replacement)')
print(task_4())
