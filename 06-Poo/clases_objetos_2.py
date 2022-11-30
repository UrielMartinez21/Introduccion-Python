class taco:
    salsa=False
    def __init__(self,sabor=None,tipo=None):
        self.sabor=sabor
        self.tipo=tipo
        print(f"-->Se creo el taco de {self.sabor} con textura {self.tipo}")
    def con_salsa(self):
        self.salsa=True
    def sin_salsa(self):
        self.salsa=False
    def tiene_salsa(self):
        if(self.salsa):
            print(f"El taco de {self.sabor} tiene salsa")
        else:
            print(f"El taco de {self.sabor} no tiene salsa")

t=taco("suadero","crujiente")
t1=taco("tripa","normal")
print(f"\nEl taco de {t.sabor} tiene salsa? {t.salsa}")
t.con_salsa()
print(f"\nEl taco de {t.sabor} tiene salsa? {t.salsa}\n")
t.sin_salsa()
print(f"\nEl taco de {t.sabor} tiene salsa? {t.salsa}\n")
t.tiene_salsa()

class catalogo_tacos:
    l_tacos=[]
    def __init__(self, l_tacos=[]):
        self.l_tacos=l_tacos
        print("Se creo la lista de tacos")

    def agregar_taco(self,tac):
        self.l_tacos.append(tac)

    def mostrar_tacos(self):
        print("Lista de tacos:")
        for i in self.l_tacos:
            print(f"\t*Taco de {i.sabor}")

c=catalogo_tacos([t])
c.agregar_taco(t1)
c.agregar_taco(taco("carnitas","normal"))
c.mostrar_tacos()