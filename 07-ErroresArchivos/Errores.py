lista=[1,2,3]
try:                                    # Dentro de try todo lo que pudiera generar error
    print(lista[9])                    
except IndexError:                      # En caso que no se pueda mostrara esto
    print("El rango se paso") 
except NameError:                       # En caso que no exita la variable
    print("No existe la variable")
except:
    print("Hubo un error")              # Error por defecto