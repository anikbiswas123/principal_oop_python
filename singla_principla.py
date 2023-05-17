# class person:
#
#     # manage the properties
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'person name is {self.name} '
#
#     # database
#     @classmethod
#     def save(cls, person):
#         print(f'Save the {person} to the database')
#
#
# p = person("sumilon")
# person.save(p)


# user
# class person:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# #database
# class Dbperson:
#
#     def sQlsave(self, p):
#         print(f"person name is {p} database save SQL")
#
#     def PostgarSql(self, p):
#         print(f"person name is {p} database save PostGarSql")
#
#     def Oracal(self, p):
#         print(f"person name is {p} database save Oracal")
#
#
# per = person("Rasel")
#
# Db = Dbperson()
# Db.sQlsave(per)
# Db.PostgarSql(per)
# Db.Oracal(per)

class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')

    def PostgarSql(self, person):
        print(f"person name is {p} database save PostGarSql")

    def Oracal(self, person):
        print(f"person name is {p} database save Oracal")


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)
        self.db.PostgarSql(person=self)
        self.db.Oracal(person=self)


p = Person('John Doe')
p.save()
