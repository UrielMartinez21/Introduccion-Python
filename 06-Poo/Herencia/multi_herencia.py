#----------------------- Clases Padres -----------------------
class A:
    def __init__(self):
        print("Soy clase A")
    def metodo_a(self):
        print("este metodo lo hereda la clase A")

class B:
    def __init__(self):
        print("Soy clase B")

    def metodo_b(self):
        print("este metodo lo hereda la clase b")

#----------------------- Clases Padres -----------------------
class C(A,B):                       #se pasan 2 clases a la clase 'c'
    def metodo_c(self):
        print("Soy metodo de C")               

#----------------------- Ejecucion -----------------------
objeto_c=C()                     #por tener metodos/atributos iguales
objeto_c.metodo_a()
objeto_c.metodo_b()