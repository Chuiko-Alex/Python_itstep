"""
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
            Задание 1

Создайте класс Device, который содержит информа-
цию об устройстве.

С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы."""



# class Device:
#     def __init__(self):
#         self.name = 'haha'
#         self.color = ''
#         self.material = ''
#         self.brand = ''
#         self.price = 0
#
#     def input_all(self):
#         self.name = input("Введите название: ")
#         self.color = input("Введите цвет: ")
#         self.material = input("Введите материал из чего изготовлен: ")
#         self.brand = input("Введите название бренда: ")
#         self.price = input("Введите цену: ")



"""
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине)
Каждый из классов должен содержать необходимые
для работы методы"""



# class Coffee_Machine(Device):
#     def print_all(self):
#         print(f'''
#     Название кофе машины: {self.name}
#     Цвет кофе машины: {self.color}
#     Материал кофе машины: {self.material}
#     Бренд кофе машины: {self.brand}
#     Цена кофе машины: {self.price}''')
#
#
#     def get_name(self):
#         return self.name
#     def get_color(self):
#         return self.color
#     def get_material(self):
#         return self.material
#     def get_brand(self):
#         return self.brand
#     def get_price(self):
#         return self.price
#
#     def set_name(self, name):
#         self.name = name
#     def set_color(self, color):
#         self.color = color
#     def set_material(self, material):
#         self.material = material
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_price(self, price):
#         self.price = price
#
#
# device_coffee_Machine = Coffee_Machine()
# device_coffee_Machine.input_all()
# device_coffee_Machine.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(device_coffee_Machine.get_name())
# device_coffee_Machine.print_all()



"""
С помощью механизма наследования, реализуйте класс
Blender (содержит информацию о кофемашине)
Каждый из классов должен содержать необходимые
для работы методы"""



# class Blender(Device):
#     def print_all(self):
#         print(f'''
#     Название блендера: {self.name}
#     Цвет блендера: {self.color}
#     Материал блендера: {self.material}
#     Бренд блендера: {self.brand}
#     Цена блендера: {self.price}''')
#
#
#     def get_name(self):
#         return self.name
#     def get_color(self):
#         return self.color
#     def get_material(self):
#         return self.material
#     def get_brand(self):
#         return self.brand
#     def get_price(self):
#         return self.price
#
#     def set_name(self, name):
#         self.name = name
#     def set_color(self, color):
#         self.color = color
#     def set_material(self, material):
#         self.material = material
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_price(self, price):
#         self.price = price
#
# device_blender = Blender()
# device_blender.input_all()
# device_blender.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(device_blender.get_name())
# device_blender.print_all()



"""
С помощью механизма наследования, реализуйте класс
MeatGrinder (содержит информацию о кофемашине)
Каждый из классов должен содержать необходимые
для работы методы"""



# class MeatGrinder(Device):
#     def print_all(self):
#         print(f'''
#     Название мясорубки: {self.name}
#     Цвет мясорубки: {self.color}
#     Материал мясорубки: {self.material}
#     Бренд мясорубки: {self.brand}
#     Цена мясорубки: {self.price}''')
#
#
#     def get_name(self):
#         return self.name
#     def get_color(self):
#         return self.color
#     def get_material(self):
#         return self.material
#     def get_brand(self):
#         return self.brand
#     def get_price(self):
#         return self.price
#
#     def set_name(self, name):
#         self.name = name
#     def set_color(self, color):
#         self.color = color
#     def set_material(self, material):
#         self.material = material
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_price(self, price):
#         self.price = price
#
# device_meat_grinder = MeatGrinder()
# device_meat_grinder.input_all()
# device_meat_grinder.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(device_meat_grinder.get_name())
# device_meat_grinder.print_all()



"""
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
                  Задание 2
Создайте класс Ship, который содержит информацию
о корабле.
С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате), класс
Destroyer (содержит информацию об эсминце), класс
Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые
для работы методы."""



# class Ship:
#     def __init__(self):
#         self.name = ''
#         self.brand = ''
#         self.year = 0
#         self.speed = 0
#         self.price = 0
#         self.color = ''
#
#     def input_all(self):
#         self.name = input("Введите название коробля: ")
#         self.brand = input("Введите марку коробля: ")
#         self.year = input("Введите год выпуска коробля: ")
#         self.speed = input("Введите скорость коробля: ")
#         self.price = input("Введите цену коробля: ")
#         self.color = input("Введите цвет коробля: ")



"""С помощью механизма наследования, реализуйте
класс Frigate (содержит информацию о фрегате)
Каждый из классов должен содержать необходимые
для работы методы."""



# class Frigate(Ship):
#     def print_all(self):
#         print(f'''
#     Название коробля: {self.name}
#     Марка коробля: {self.brand}
#     Год выпуска коробля: {self.year}
#     Скорость коробля: {self.speed}
#     Цена коробля: {self.price}
#     Цвет коробля: {self.color}''')
#
#     def get_name(self):
#         return self.name
#     def get_brand(self):
#         return self.brand
#     def get_year(self):
#         return self.year
#     def get_speed(self):
#         return self.speed
#     def get_price(self):
#         return self.price
#     def get_color(self):
#         return self.color
#
#     def set_name(self, name):
#         self.name = name
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_year(self, year):
#         self.year = year
#     def set_speed(self, speed):
#         self.speed = speed
#     def set_price(self, price):
#         self.price = price
#     def set_color(self, color):
#         self.color = color
#
# frigate_ship = Frigate()
# frigate_ship.input_all()
# frigate_ship.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(frigate_ship.get_name())
# frigate_ship.print_all()



"""С помощью механизма наследования, реализуйте
класс Destroyer (содержит информацию о фрегате)
Каждый из классов должен содержать необходимые
для работы методы."""



# class Destroyer(Ship):
#     def print_all(self):
#         print(f'''
#     Название коробля: {self.name}
#     Марка коробля: {self.brand}
#     Год выпуска коробля: {self.year}
#     Скорость коробля: {self.speed}
#     Цена коробля: {self.price}
#     Цвет коробля: {self.color}''')
#
#     def get_name(self):
#         return self.name
#     def get_brand(self):
#         return self.brand
#     def get_year(self):
#         return self.year
#     def get_speed(self):
#         return self.speed
#     def get_price(self):
#         return self.price
#     def get_color(self):
#         return self.color
#
#     def set_name(self, name):
#         self.name = name
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_year(self, year):
#         self.year = year
#     def set_speed(self, speed):
#         self.speed = speed
#     def set_price(self, price):
#         self.price = price
#     def set_color(self, color):
#         self.color = color
#
# destroyer_ship = Destroyer()
# destroyer_ship.input_all()
# destroyer_ship.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(destroyer_ship.get_name())
# destroyer_ship.print_all()



"""С помощью механизма наследования, реализуйте
класс Destroyer (содержит информацию о фрегате)
Каждый из классов должен содержать необходимые
для работы методы."""



# class Cruiser(Ship):
#     def print_all(self):
#         print(f'''
#     Название коробля: {self.name}
#     Марка коробля: {self.brand}
#     Год выпуска коробля: {self.year}
#     Скорость коробля: {self.speed}
#     Цена коробля: {self.price}
#     Цвет коробля: {self.color}''')
#
#     def get_name(self):
#         return self.name
#     def get_brand(self):
#         return self.brand
#     def get_year(self):
#         return self.year
#     def get_speed(self):
#         return self.speed
#     def get_price(self):
#         return self.price
#     def get_color(self):
#         return self.color
#
#     def set_name(self, name):
#         self.name = name
#     def set_brand(self, brand):
#         self.brand = brand
#     def set_year(self, year):
#         self.year = year
#     def set_speed(self, speed):
#         self.speed = speed
#     def set_price(self, price):
#         self.price = price
#     def set_color(self, color):
#         self.color = color
#
# cruiser_ship = Cruiser()
# cruiser_ship.input_all()
# cruiser_ship.set_name('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
# print(cruiser_ship.get_name())
# cruiser_ship.print_all()





"""
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
            Задание 3

Запрограммируйте класс Money (объект класса опе-
рирует одной валютой) для работы с деньгами.

В классе должны быть предусмотрены поле для хра-
нения целой части денег (доллары, евро, гривны и т.д.) и

поле для хранения копеек (центы, евроценты, копейки
и т.д.).

Реализовать методы для вывода суммы на экран, за-
дания значений для частей.

Я добавил сложности в ваше задание и решил реализовать это в виде
мине обменки, что бы по выбору пользователя совершал обмен, пользователь должен выбрать
1 - это гривна
2 - это доллар
3 - это евро"""



# class Money:
#     def __init__(self):
#         self.money = 0
#         self.hryvnia = 0
#         self.dollar = 0
#         self.euro = 0
#         self.hryvnia_penny = 0
#         self.dollar_penny = 0
#         self.euro_penny = 0
#         self.currency = 0

#     def euros_exchange(self, money, currency):
#         if currency == 1:
#             self.euro = money // 30
#             self.euro_penny = money % 30
#             return f"При обмене {money} гривень на евро вы получите: {self.euro}евро {self.euro_penny}цента"
#         if currency == 2:
#             self.euro = int(money // 1.2)
#             self.euro_penny = round(money % 1.2, 3)
#             return f"При обмене {money} долларов на евро вы получите: {self.euro}евро {self.euro_penny}цента"
#
#     def dollar_exchange(self, money, currency):
#         if currency == 1:
#             self.dollar = money // 27
#             self.dollar_penny = money % 27
#             return f"При обмене {money} гривень на доллар вы получите: {self.dollar}долларов {self.dollar_penny}цента"
#         if currency == 3:
#             self.dollar = int(money // 0.83)
#             self.dollar_penny = round(money % 0.83, 3)
#             return f"При обмене {money} евро на доллары вы получите: {self.dollar}долларов {self.dollar_penny}цента"
#
#     def hryvnia_exchange(self, money, currency):
#         if currency == 2:
#             self.hryvnia = int(money * 27)
#             self.hryvnia_penny = (money * 27) % 1
#             return f"При обмене {money} долларов на гривну вы получите: {self.hryvnia}гривень {self.hryvnia_penny}коппек"
#         if currency == 3:
#             self.hryvnia = int(money * 30)
#             self.hryvnia_penny = round((money * 30) % 1, 3)
#             return f"При обмене {money} евро на гривну вы получите: {self.hryvnia}гривень {self.hryvnia_penny}коппек"
#
# money_exchange = Money()
# print(money_exchange.euros_exchange(123663, 1))
# print(money_exchange.euros_exchange(1233, 2))
# print()
# print(money_exchange.dollar_exchange(123663, 1))
# print(money_exchange.dollar_exchange(1233, 3))
# print()
# print(money_exchange.hryvnia_exchange(10, 2))
# print(money_exchange.hryvnia_exchange(10, 3))
