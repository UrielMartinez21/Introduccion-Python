#------------------------- Clase Padre -------------------------
class Persona:
    def __init__(self,nombre,edad):     # Clase constructora
        self.nombre=nombre
        self.edad=edad
        print("[+]Se creo la clase")

    def mostrar_datos(self):            # Clase creada por el usuario
        print(f"\tNombre: {self.nombre}\n\tEdad: {self.edad}")

    def __str__(self):                  # Clase que muestra el estado del objeto
        return f"Los datos son: {self.nombre} y {self.edad}"

#------------------------- Clase Hijo -------------------------
# Recibe como parametro la clase padre
class Hombre(Persona):
    pass

#------------------------- Herencia Super -------------------------
# Recibe funciones de la clase padre
class Maestro(Persona):
    def __init__(self, nombre, edad,sueldo):
        super().__init__(nombre, edad)          # Traemos atributos de la clase padre
        self.sueldo=sueldo                      # Agregamos un atributo adicional

    def mostrar_empleado(self):
        super().mostrar_datos()                 # Traemos la funcion de la clase padre
        print(f"\tEl sueldo es: {self.sueldo}") # Concatenamos el resultado con este print

    def __str__(self):
        return super().__str__() + f" y el sueldo es: {self.sueldo}"

#------------------------- Herencia sin Super -------------------------
# Recibe funciones de la clase padre
class Alumno(Persona):
    def __init__(self, nombre, edad,califi):
        Persona.__init__(self,nombre, edad)     # Traemos atributos de la clase padre
        self.califi=califi                      # Agregamos un atributo adicional

    def mostrar_alumno(self):
        Persona.mostrar_datos(self)           # Traemos la funcion de la clase padre
        print(f"\tCalifi: {self.califi}")       # Concatenamos el resultado con este print

    def __str__(self):
        return Persona.__str__(self) + f" y la calicacion es: {self.califi    }"


