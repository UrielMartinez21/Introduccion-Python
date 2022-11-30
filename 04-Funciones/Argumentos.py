#-------------------- Argumentos indeterminados --------------------
# '*args' = posicionamiento   '**kwargs' = nombre
def Sumar(*args, **kwargs):
    print(f"Los argumentos son: {args}")
    suma=0
    for x in args:
        suma+=x
    return suma, kwargs

suma_total,datos=Sumar(1,2,3,4,5,6, nombre="vecino", edad=20)
print(f"El total es: {suma_total}")
print(f"Los datos son: {datos}")