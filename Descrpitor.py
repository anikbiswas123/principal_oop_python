# class Descriptor(object):
#
#     def __init__(self, name=''):
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         return self.name
#
#     def __set__(self, obj, name):
#         if isinstance(name, str):
#             self.name = name
#         else:
#             raise TypeError("Name should be string")
#
#
# class GFG(object):
#     name = Descriptor()


# g = GFG()
# g.name = 123
# print(g.name)


class Descriptor(object):
    def __init__(self,name=''):
        self.name=name

    def __get__(self, obj, objtype):
        return self.name

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")

class person(object):
     name=Descriptor(object)



p=person()
p.name='BTV'
print(p.name)




