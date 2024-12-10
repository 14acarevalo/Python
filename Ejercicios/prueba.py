try:
    numero = int(input("Usuario, introduce un número: "))
    print(f"El número introducido es: {numero}")
except ValueError:
    print("El valor introducido no es un número válido.")
