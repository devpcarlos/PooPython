class Celular:
    #metodo constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


    def llamar(self):
        print(f"estas llamado desde un: {self.marca} {self.modelo} {self.camara}")

celular1 = Celular("Xiaomi","MIUI","120MP")

print(celular1.modelo)
celular1.llamar()

