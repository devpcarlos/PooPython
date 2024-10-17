class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def names(self):
        return self.name

    @names.setter
    def names(self, new_name):
        self.name = new_name

    @names.deleter
    def names(self):
       del self.name

nombre =Persona("John", 25)
print(nombre.name)

del nombre.names