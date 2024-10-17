class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name=new_name

nombre =Persona("John", 25)
print(nombre.get_name())

nombre.set_name("Mary")
print(nombre.get_name())