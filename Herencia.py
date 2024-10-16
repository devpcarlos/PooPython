from Estudiante import nombre

#Clase padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad ):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista :
    def __init__(self, habilidad ):
        self.habilidad = habilidad

    def mostrar_hsbilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

#herencia multiple
class EmplaedoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa ):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f'{super().mostrar_hsbilidad()}'

persona = EmplaedoArtista("carlos", 30, "colombiano","programar",500000,"tecnologia")
persona.presentarse()

#Herencia
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad, trabajo, salario ):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("carlos", 30, "colombiano","programar",500000)
print(roberto.nombre)