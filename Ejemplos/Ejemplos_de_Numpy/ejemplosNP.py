import numpy as np                  #Se importa numpy como np 
lista = [25, 16, 9, 4, 1]           #Se crea una lista y se le asignan valores
vector = np.array(lista)            #Se le asigna a vector la funcion de numpy y se le pasa a lista como atributo
print(vector)


arr=np.zeros((2,3),dtype=int)       #Imprime una matriz con puros 0's
print(arr)

print(np.sqrt(vector))              #saca la raiz cuadrada de cada elemento dentro del arreglo