import random

##Ejercicio 1 - Vamos a contar hasta 10

variable = 1

while (variable <=10) :
    print(variable)
    variable += 1

print("")
    
##Ejercicio 2: Pedir un numero al usuario y calcular toda la suma de los numeros ahi presentes

print("Usuario, te necesito")
numero= (int(input("Dame un numero y calcularemos la suma que hay del 0 hasta ese numero ")))
suma = 0
comienzo = 0
suma = suma+comienzo
while (comienzo<=numero) :
    suma = suma+comienzo
    comienzo+=1
    
print(suma)
print("")

##Ejercicio 3: Realizar un programa que imprima números impares del 1 al 50

comienzo1 = 1

print("Bienvenido a este programa fantástico, donde vamos a imprimir números del 1 al 50")
while comienzo1 <= 50:
    if comienzo1 % 2 != 0:
        print(comienzo1)
    comienzo1= comienzo1+1
print(" ")   
##Ejercicio 4: Contador de dígitos

print("Usuario, vamos a contar los digitos de tú número")
numero_Contar = int(input("Introduce un número por favor: "))

contadorNumeros = 0

while numero_Contar != 0 :
    numero_Contar = numero_Contar//10
    contadorNumeros += 1
print(str(contadorNumeros))
print(" ")

##Ejercicio 5: Adivinar el numero
intentos = 0
vidas = 5
numeroOculto = random.randint(1, 14)  # Generar el número oculto entre 1 y 14

# Solicitar el primer número al usuario
numeroUsuario = int(input("Usuario, adivina el número mágico que se encuentra entre el 1 y el 14: "))

while vidas > intentos:
    if numeroUsuario < 1 or numeroUsuario > 14:
        print("Usuario, ese número se encuentra fuera del intervalo ubicado entre 1 y 14. Intenta de nuevo.")
    else:
        if numeroUsuario > numeroOculto:
            print("Usuario, el número que has escogido es más grande que el número mágico.")   
        elif numeroUsuario < numeroOculto:
            print("Usuario, el número oculto es más grande.")
        else:
            print("Enhorabuena!!! HAS ACERTADOOOOO!!!")
            break
        
        intentos += 1
        vidasRestantes = vidas - intentos
        print(f"Vaya, has perdido una vida, te quedan {vidasRestantes} vidas.")
        
        if vidasRestantes == 0:
            print(f"Lo siento, has agotado todas tus vidas. El número mágico era {numeroOculto}.")
            break
    
    if vidas > intentos:
        numeroUsuario = int(input("Usuario, intentalo de nuevo: "))

if vidas == intentos:
    print(f"Lo siento, has agotado todas tus vidas. El número mágico era {numeroOculto}.")
    
print("")

##Ejercicio 6: Imprimir números pares del 1 al 50
numero = 1
print("Usuario, vamos a imprimir números comprendidos entre el 1 y 50, pero en este caso serán pares")
while numero <=50:
    if numero % 2==0:
        print("Los números pares de este intervalo son: " +str(numero))
    numero += 1

print("")

##Ejercicio 7: Suma de números
comienzo = 1
suma = 0
print("En este ejercicio, vamos a imprimir los números del 1 al 100 con bucle while y además, vamos a realizar la suma de todos ellos")
while comienzo <=100:
    print("El numero es " +str(comienzo))
    comienzo += 1
    suma = suma + comienzo
print("")
print("El resultado de sumar todos los números es igual a: " +str(suma))
print(" ")

##Ejercicio 8: Factorial de los números hasta 100
    
comienzo1 = 1
factorial = 1
print("En este ejercicio, vamos a imprimir los números del 1 al 100 con bucle while y además, vamos a realizar el factorial de todos ellos")
while comienzo1 <=100:
    print("El numero es " +str(comienzo1))
    factorial = factorial* comienzo1
    comienzo1 += 1

print("")
print("El factorial de todos los números es igual a: " +str(factorial))
print(" ") 


##Ejercicio 9: El factorial del número introducido 

comienzo2 = 1
factorial1 = 1

print("Usuario, vamos a realizar el factorial del número que introduzcas")
numeroUsuario = int(input("Introduce un numero: "))

while comienzo2 <= numeroUsuario:
    factorial1 = factorial1*comienzo2
    comienzo2 += 1

print("El factorial del número " +str(numeroUsuario)+ " que tu has introducido, es igual a: " +str(factorial1))
print("")

##Ejercicio 10: Feliz año nuevo!!!

print("Usuario, vamos a dar la bienvenida al próximo año")
contadorAño = 10

while (contadorAño >= 0):
    print(contadorAño)
    contadorAño -= 1
print("Feliz año nuevo!!!!!!!!")
print(" ")

##Ejercicio 11: Adivina la contraseña

contraseña = "Contraseña1234"
intentos = 0
print("Usuario, en este programa vas a tener que introducir tu contraseña")
contraseñaUsuario = " "
while contraseñaUsuario != contraseña :
    contraseñaUsuario = input("Usuario, introduce la contraseña: ")
    intentos +=1
    if contraseñaUsuario != contraseña :
        print("Usuario, esa no es la contraseña, piensa ")
print("PREMIO!!!!!!!!!! esa es la contraseña, sólo has necesitado " +str(intentos)+ " intentos")
print(" ")

def es_primo(n):
    if n <= 0:
        return False
    if n == 2:
        return True
    if n % 2 != 0:
        return True
    

while True:
    number = int(input("Usuario introduce un número "))
    if number <= 0:
        print("Programa finalizado")
        break
    if es_primo(number):
        print("El número introducido es primo ")