class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def estudiar(self):
        print("Estudiando...")

nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese el edad: ")

estudiante = Estudiante(nombre,apellido,edad )

print(f"""
Datos del estudiante: \n\n
nombre: {estudiante.nombre}\n
apellido: {estudiante.apellido}\n
edad: {estudiante.edad}\n
""")

