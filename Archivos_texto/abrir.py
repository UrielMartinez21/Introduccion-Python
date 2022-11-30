#Abrir archivo de texto en modo lectura por defecto si no se especifica
#       archivo=open("escritura.txt")
archivo=open("escritura.txt","r")

#Leer todo el archivo de texto
print(archivo.read())

#Comprobar si un archivo se puede leer
print(f"Se puede leer el archivo: {archivo.readable()}\n")

#Despues de abrir el archivo se debe cerrar
#Con with se cierra solo el archivo en automatico
archivo.close()

###############################################################
#Mejor forma de abrir y cerrar archivo
# Si no se especifica el modo sera por defecto de lectura
with open("escritura.txt") as texto:
    print(f"Se puede leer el archivo: {texto.readable()}\n")
    print(texto.read())