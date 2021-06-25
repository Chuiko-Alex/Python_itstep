import json

"""
                   Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).
"""

class Countries_and_capitals:
    def __init__(self):
        self.dict_all = {'Ukraine':'Kiev', 'Russia':'Moskov', 'Algeria':'Algeria', 'Angola':'Luanda' }
        self.countries = ""
        self.capitals = ""

    def add(self, countries, capitals):
        self.dict_all[countries] = capitals

    def delete(self, countries):
        del self.dict_all[countries]

    def search(self, countries):
        if countries in self.dict_all:
            return f'{countries}, Есть в словаре'
        else:
            return f'{countries}, Нет в словаре'

    def editing_capitals(self, countries, new_capitals):
        self.dict_all[countries] = new_capitals

    def editing_countries(self, countries, new_countries):
        self.dict_all[new_countries] = self.dict_all.pop(countries)

    def get_dict_all(self):
        return self.dict_all

    def json_dumps(self):
        with open('dumps.json', 'w+') as f:
            json.dump(self.dict_all, f)



a = Countries_and_capitals()
a.add("Hi", "Ha")
a.delete("Ukraine")
a.json_dumps()
print(a.search("Russia"))

print(a.get_dict_all())
