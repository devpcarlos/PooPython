from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, name, edad, trabaja):
        self.name = name
        self.edad = edad
        self.trabaja = trabaja

    @abstractclassmethod
    def trabaja(self):
        pass

    def presentarse(self):
        print(f" Hola, me llamo: {self.name} y tengo {self.edad} años")

class Estudinate(Persona):
    def __init__(self, name, edad, trabaja):
        super().__init__(name, edad, trabaja)

    def trabaja(self):
        pass

carlos= Estudinate("Carlos", 19, "Programador")

carlos.presentarse()