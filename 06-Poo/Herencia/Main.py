#------------------------- Libreria -------------------------
from Herencia import Hombre,Maestro,Alumno

#------------------------- Clase Heredada -------------------------
hombre1=Hombre("Juan",39)
hombre1.mostrar_datos()
print(hombre1)

#------------------------- Herencia Super -------------------------
print("\n")
maestro1=Maestro("Alex",93,5000)
maestro1.mostrar_empleado()
print(maestro1)

#------------------------- Herencia sin Super -------------------------
print("\n")
alumno1=Alumno("Pedro",18,10)
alumno1.mostrar_alumno()
print(alumno1)