from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
a=[1,2,3]
b=[10,20,30]
#configuracion
plt.plot(a, label="Linea 1", linewidth=4, color="red")
plt.plot(b, label="Linea 2", linewidth=4, color="blue")
#plt.bar(a,b, label="Linea 2", width=4, color="blue")

#titulo y nombre de ejes
plt.title("Diagrama")
plt.ylabel("eje y")
plt.xlabel("eje x")
#leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()