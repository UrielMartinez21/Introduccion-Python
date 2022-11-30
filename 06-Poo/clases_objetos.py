#una clase es un molde para algun objeto
class tamal:
    pass                                                    #para argumentos vacios
tamal_de_fresa=tamal()                                      
tamal_de_fresa.sabor='fresa'                                #despues del punto es considerardo 'atributo' de la clase
print(f"El sabor del tamal es de {tamal_de_fresa.sabor}")   

print("\n-----------termino la primer clase-----------\n")

class torta:                                                #esto es una clase
    glaseado=False                                          #init es metodo constructor
    def __init__(self):                                     #esto es un metodo
        print('Se creo la clase')
    def glasear(self):                                      #self hace referencia al objeto que se creara
        self.glaseado=True                                  #el glaseado del atributo que se creara
    def esta_glaseada(self):
        if(self.glaseado):
            print("La torta es glaseada")
        else:
            print("La torta no esta glaseada")

t=torta()                                                   #aqui se creo 't' de la clase 'torta'
print(t.glaseado,"\n")                                      #se imprime el atributo glaseado(dara falso)
t.glasear()                                                 #asi se llama un metodo
print(t.glaseado)
t.esta_glaseada()                                           #no hace falta el print' ya que en la funcion esta print

print("\n-----------termino la segunda clase-----------\n")

class taco:
    salsa=False
    def __init__(self,tipo=None,color=None):                #los valores por defecto seran vacios
        self.tipo=tipo
        self.color=color
        if tipo is not None and color is not None:
            print(f"Se creo un taco de {self.tipo} con color {self.color}")
        else:
            print("Se creo una taco cualquiera")
    def con_salsa(self):
        self.salsa=True
    def tiene_salsa(self):
        if(self.salsa):
            print("El taco tiene salsa")
        else:
            print("El taco no tiene salsa")

taco1=taco('suadero','amarillo')
print(taco1.salsa)
taco1.con_salsa()
print(taco1.salsa)
taco1.tiene_salsa()

print("\n-----------termino la tercera clase-----------\n")

class rectangulo:
    def __init__(self,lado,ancho):
        self.lado=lado
        self.ancho=ancho
        print("Se creo el rectangulo")
    def area(self):
        r_area=self.ancho*self.lado
        return r_area                                       #alternativa para devolver valores en vez de imprimirlo
    def perimetro(self):
        r_perimetro=(2*self.ancho)+(2*self.lado)
        return r_perimetro
    def __del__(self):                                      #metodo destructor
        print(f"Se elimino el rectangulo con lado: {self.lado} y ancho: {self.ancho}")


r=rectangulo(2,3)
print(f"El area del rectangulo es {r.area()}")
print(f"El perimetro del rectangulo es {r.perimetro()}")
del(r)                                                      #se llama al metodo destructor