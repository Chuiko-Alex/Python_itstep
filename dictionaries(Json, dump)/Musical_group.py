import json


'''
Задание 2
Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку).
'''


class Musical_group:
    def __init__(self):
        self.dict_all = {'Led Zeppelin':'Good Times Bad Times', 'The Who':'Overture', 'The Stooges':'1969', 'MC5':"Ramblin' Rose" }
        self.name_group = ""
        self.album = ""

    def add(self, name_group, album):
        self.dict_all[name_group] = album

    def delete(self, name_group):
        del self.dict_all[name_group]

    def search(self, name_group):
        if name_group in self.dict_all:
            return f'{name_group}, Есть в словаре'
        else:
            return f'{name_group}, Нет в словаре'

    def editing_capitals(self, name_group, new_album):
        self.dict_all[name_group] = new_album

    def editing_countries(self, name_group, new_group):
        self.dict_all[new_group] = self.dict_all.pop(name_group)

    def get_dict_all(self):
        return self.dict_all

    def json_dumps(self):
        with open('dumps_m.json', 'w+') as f:
            json.dump(self.dict_all, f)


a = Musical_group()
a.add("The Kinks", "Victoria")
a.delete("Led Zeppelin")
a.json_dumps()
print(a.search("The Kinks"))

print(a.get_dict_all())
