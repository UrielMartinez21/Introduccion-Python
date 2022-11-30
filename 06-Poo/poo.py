productos=[
    {'cod':'10001', 'nombre': 'Jabon armony', 'categoria':'higiene personal','pvp':0.9},
    {'cod':'10002', 'nombre': 'Cereal', 'categoria':'comida','pvp':1.2},
    {'cod':'10003', 'nombre': 'Limones', 'categoria':'fruta','pvp':0.3},
    {'cod':'10004', 'nombre': 'Fresas', 'categoria': 'fruta', 'pvp': 0.5}
]

def mostrar_producto(productos, cod):
    for p in productos:                                             #p va obteniendo el valor de cada indice
        if (cod==p['cod']):                                         #Si cod es igual al indice del valor cod
            return print(f"\n-->{p['nombre']}= ${p['pvp']}")
    print("\nEl producto no existe")

def eliminar_producto(productos,cod):
    for i, p in enumerate(productos):
        if(cod==p['cod']):
            del(productos[i])
            return print(str(p),"eliminado")
    print("producto no encontrado")

def buscar_producto(productos,cod):
    for p in productos:
        if(cod==p['cod']):
            return print("El producto existe")
    print("El producto no se encuentra")

print(productos)
# mostrar_producto(productos,'10002')
#eliminar_producto(productos,'10002')
#buscar_producto(productos,'10002')

numeros_d=[1,2,3,4,5,6]
def buscar_numero(numeros_d,num):
    for i in numeros_d:
        if(num==i):
            return print(f"\nEl numero {num} existe")
    print(f"\nEl numero {num} no existe")

# x=int(input("Ingresa el numero que desea buscar en la lista(1,...,6): "))
# buscar_numero(numeros_d,x)