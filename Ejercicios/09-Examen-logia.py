##Examen con if - for - while

## Ejercicio 1 - Escribe un programa que pida al usuario un número entero y determine si el número es positivo, negativo o cero.
print("Ejercicio 1, vamos crear un programa en donde busquemos que el numero sea mayor que 0 y en función del número introducido veremos que tipo es")
numeroUsuario = int(input("Usuario, introduce un número: "))

if numeroUsuario >= 0 :
    if numeroUsuario == 0:
        print("El número introducido es 0")
    else:
        print("El numero introducido es positivo mayor que 0")
else:
    print("El numero es negativo")

print(" ")
    
##Ejercicio 2 - Escribe un programa que pida al usuario una contraseña. El programa debe seguir pidiendo la contraseña hasta que el usuario introduzca "Contraseña1234".

print("Usuario, introduce tu contraseña: ")
contraseña = "Contraseña1234"
pruebaContraseña = " "
intentos = 0

while contraseña !=pruebaContraseña :
    pruebaContraseña = input("Usuario introduce la contraseña: ")
    if pruebaContraseña == contraseña:
        print("Contraseña correcta!")
    else:
        print("Prueba otra vez ")
        
    intentos += 1
print("Has necesitado " +str(intentos)+ " intentos")

print(" ")

##Ejercicio 3 - Escribe un programa que pida al usuario un número entero y luego imprima la tabla de multiplicar de ese número del 1 al 10.
print("En este ejercicio, vamos a realizar una tabla de multiplicar de un número determinado, el que tu introduzcas")
numeroMultiplicar = int(input("Usuario, introduce un número: "))
multiplicacion = 0

for numero in range (1, (10+1)):
    print("La tabla de multiplicar del número " +str(numeroMultiplicar))
    multiplicacion = numeroMultiplicar * numero
    print (str(numeroMultiplicar)+ " x " +str(numero)+ " = " +str(multiplicacion))
print(" ")

##Ejercicio 4 - Escribe un programa que pida al usuario una frase y cuente cuántas vocales (tanto mayúsculas como minúsculas) hay en la frase.

print("En este ejercicio vamos a contar vocales ")
vocales = "aeiouAEIOU"
contadorVocales = 0
frase = input("Que frase me vas a decir usuario: ")

for letra in frase:
    if letra in vocales:
        contadorVocales += 1
print("En tu frase hay " +str(contadorVocales)+ " vocales")
print(" ")

##Ejercicio 5 - Operaciones con listas
listaNumeros = []

print("Usuario, introduce 5 numeros ")
for numero in range (1, (5+1)):
    num = int(input())
    listaNumeros.append(num)
    
print("La lista completa de los números es "+str(listaNumeros))
print("La suma total es igual a : " +str(sum(listaNumeros)))
print("El número más grande es: " +str(max(listaNumeros)))
print("El número más pequeño es: " +str(min(listaNumeros)))

