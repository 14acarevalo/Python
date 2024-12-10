print("En este programa, vamos a realizar un programa para transformar un número que introduzca el usuario a binario: ")

# Solicitar al usuario que introduzca un número decimal
num = int(input("Usuario, introduce un número por favor: "))

# Inicializar la variable para almacenar el número binario
binario = ""

# Bucle para convertir el número decimal a binario
while num > 0:
    resto = num % 2
    binario = str(resto) + binario
    num = num // 2

print("El número binario es igual a: " + binario)

    