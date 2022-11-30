class punto:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y
        if (self.x is not None and self.y is not None):
            print("Se creo el punto...!")
        else:
            print("El valor es 0")
    def mostrar_punto(self):
        print(f"La coordenada es: ({self.x},{self.y})")
    def cuadrante(self):
        if(self.x>0 and self.y>0):
            print("El punto se encuentra en el primer cuadrante")
        elif(self.x<0 and self.y>0):
            print("El punto se encuentra en el segundo cuadrante")
        elif(self.x < 0 and self.y < 0):
            print("El punto se encuentra en el tercer cuadrante")
        elif(self.x > 0 and self.y < 0):
            print("El punto se encuentra en el cuarto cuadrante")
        else:
            print("El punto no esta en ningun cuadrante")
p=punto(3,-1)
p.mostrar_punto()
p.cuadrante()
