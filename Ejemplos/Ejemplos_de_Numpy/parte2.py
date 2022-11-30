from re import A
import numpy as np

a=np.array([1,2,3])
b=np.array(([1,2,3],[1,2,3]))

print(f"Arreglo unidimensional\n{a}\n")
print(f"Arreglo bidimensional\n{b}\n")

unos=np.ones((4,4))
print(f"Matriz de unos\n{unos}\n")

ceros=np.zeros((2,3))
print(f"Matriz de ceros\n{ceros}\n")

aleatorio=np.random.random((2,2))
print(f"Matriz de aleatorios\n{aleatorio}\n")