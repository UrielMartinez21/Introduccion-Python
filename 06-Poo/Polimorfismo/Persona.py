#----------------------- Clase Padre -----------------------
class Persona(object):
    def __init__(self,nombre):
        self.nombre=nombre
    def moverse(self):
        print("Caminando")

#----------------------- Clases Hijos -----------------------
class Atleta(Persona):
    def moverse(self):
        print("Corriendo")

class Ciclista(Persona):
    def moverse(self):
        print("En bicicleta")