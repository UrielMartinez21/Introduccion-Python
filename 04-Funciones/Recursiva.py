#-------------------- Funcion recursiva --------------------
def factorial(numero):
    if numero == 1:
        return 1
    else:
        numero = numero * factorial(numero - 1)
        return numero


valor = factorial(4)
print(f"El factorial es: {valor}")
