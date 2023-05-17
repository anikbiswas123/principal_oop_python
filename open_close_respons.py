# class person:
#     def __init__(self,name):
#         self.name=name
#
#     def  __str__(self):
#         return self.name
#
#
# class personStorage:
#     def Save_to_database(self,person):
#         print(f'person name {person} Save to DataBase')
#
#     def save_to_Json(self,person):
#         print(f'person name  {person} save to Json')
#
#
#
# per=person("sumilon")
# p_str=personStorage()
# p_str.save_to_Json(per)
# p_str.Save_to_database(per)

from abc import ABC, abstractmethod


class person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class personStorage(ABC):

    @abstractmethod
    def save(self, person):
        pass


class personDb(personStorage):
    def save(self, person):
        print(f'person Data save {person} database')


class personJson(personStorage):
    def save(self, person):
        print(f'person Data save {person} Json')


class personXML(personStorage):
    def save(self, person):
        print(f'person Data save {person} XML')


per = person("sumilon")
db = personDb()
db.save(per)
xml = personXML()
xml.save(per)
json = personJson()
json.save(per)
