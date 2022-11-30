# Capitulo 80 del curso
#-------------------- Libreria general --------------------
# import LibreriaSuma                   # Importamos todas las funciones de libreria
# suma=LibreriaSuma.Suma(1,2,3,4,5,6)
# print(suma)

#-------------------- Funcion en especifico --------------------
# from LibreriaSuma import Suma           # Importa funcion en especifico
# numeros=Suma(1,2,3,4,5,6)
# print(numeros)

#-------------------- Libreria con diferente nombre --------------------
import LibreriaSuma as ls
suma=ls.Suma(1,2,3,4,5,6)
print(suma)