"""            Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, произво-
дителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реа-
лизуйте доступ к отдельным полям через методы класса.
К уже реализованному классу «Автомобиль» добавьте
конструктор, а также необходимые перегруженные методы."""

# class Automobile:
#     def __init__(self):
#         self.model=''
#         self.year = 0
#         self.color = ''
#         self.price = 0
#         self.manufacturer = ''
#         self.volume = 0
#         self.do = ""
#
#     def input_all(self):
#         self.manufacturer = input('Введите производителя машины ')
#         self.model = input('Введите модель машины ')
#         self.volume = input('Введите обьем двигателя машины ')
#         self.price = input('Введите стоимость машины ')
#         self.color = input('Введите цвет машины ')
#         self.year = input('Введите год выпуска машины ')
#
#     def print_all(self):
#         print(f"Производитель машины {self.manufacturer}")
#         print(f"Модель машины {self.model}")
#         print(f"Обьем двигателя машины {self.volume}")
#         print(f"Цена машины {self.price}")
#         print(f"Цвет машины {self.color}")
#         print(f"Год выпуска машины {self.year}")
#
#     def get_manufacturer(self):
#         return self.manufacturer
#     def get_model(self):
#         return self.model
#     def get_volume(self):
#         return self.volume
#     def get_price(self):
#         return self.price
#     def get_color(self):
#         return self.color
#     def get_year(self):
#         return self.year
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#     def set_model(self, model):
#         self.model = model
#     def set_volume(self, volume):
#         self.volume = volume
#     def set_price(self, price):
#         self.price = price
#     def set_color(self, color):
#         self.color = color
#     def set_year(self, year):
#         self.year = year
#
#     def __repr__(self):
#         return self.model
#     def __str__(self):
#         return self.model
#
#
# auto_ru = Automobile()
# auto_ru.input_all()
# auto_ru.show()
# auto_ru.print_all()



"""             Задание 2
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
К уже реализованному классу «Книга» добавьте
конструктор, а также необходимые перегруженные методы."""


# class book:
#     def __init__(self):
#         self.name = ''
#         self.year = 0
#         self.publisher = ''
#         self.genre = ''
#         self.author = ''
#         self.price = 0
#
#     def input_all(self):
#         self.name = input('Введите название книги ')
#         self.year = input('Введите год выпуска книги ')
#         self.publisher = input('Введите издателя книги ')
#         self.genre = input('Введите жанр книги ')
#         self.author = input('Введите автора книги ')
#         self.price = input('Введите цену книги ')
#
#     def print_all(self):
#         print(f"Название книги {self.name}")
#         print(f"Год выпуска книги {self.year}")
#         print(f"Издатель книги {self.publisher}")
#         print(f"Жанр книги {self.genre}")
#         print(f"Автор книги {self.author}")
#         print(f"Цена книги {self.price}")
#
#     def get_name(self):
#         return self.name
#     def get_year(self):
#         return self.year
#     def get_publisher(self):
#         return self.publisher
#     def get_genre(self):
#         return self.genre
#     def get_author(self):
#         return self.author
#     def get_price(self):
#         return self.price
#
#     def set_name(self, name):
#         self.name = name
#     def set_year(self, year):
#         self.year = year
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#     def set_genre(self, genre):
#         self.genre = genre
#     def set_author(self, author):
#         self.author = author
#     def set_price(self, price):
#         self.price = price
#
#     def __repr__(self):
#         return self.name
#     def __str__(self):
#         return self.name


# book_ru = book()
# book_ru.input_all()
# book_ru.show()
# book_ru.print_all()
# book_ru.set_price("120")
# book_ru.get_price()
# print(book_ru.__str__())
# print(book_ru.__repr__())


"""             Задание 3
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
К уже реализованному классу «Стадион» добавьте
конструктор, а также необходимые перегруженные методы."""

# class Stadium:
#     def __init__(self):
#         self.name = ''
#         self.year = 0
#         self.country = ''
#         self.city = ''
#         self.capacity = 0
#
#     def input_all(self):
#         self.name = input('Введите название стадиона ')
#         self.year = input('Введите дату открытия стадиона ')
#         self.country = input('Введите страну стадиона ')
#         self.city = input('Введите город стадиона ')
#         self.capacity = input('Введите вместительность стадиона ')
#
#     def print_all(self):
#         print(f"Название стадиона {self.name}")
#         print(f"Год год открытия стадиона {self.year}")
#         print(f"Страна стадиона {self.country}")
#         print(f"Город стадиона {self.city}")
#         print(f"Вместительность стадиона {self.capacity}")
#
#
#     def get_name(self, name):
#         return self.name
#     def get_year(self, year):
#         return self.year
#     def get_country(self, country):
#         return self.country
#     def get_city(self, city):
#         return self.city
#     def get_capacity(self, capacity):
#         return self.capacity
#
#     def set_name(self, name):
#         self.name = name
#     def set_year(self, year):
#         self.year = year
#     def set_country(self, country):
#         self.country = country
#     def set_city(self, city):
#         self.city = city
#     def set_capacity(self, capacity):
#         self.capacity = capacity
#
#     def __repr__(self):
#         return self.name
#     def __str__(self):
#         return self.name
#
# Stadium_football = Stadium()
# Stadium_football.input_all()
# Stadium_football.show()
# Stadium_football.print_all()
# Stadium_football.set_name("Akvamarine")
# print(Stadium_football.get_name())