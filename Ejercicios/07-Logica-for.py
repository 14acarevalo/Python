##Ejercicio 1 - Imprimir numeros del 1 al 10

for numero in range (1, (10+1)):
    print (str(numero))
    
##Ejercicio 2 - Suma numeros del 1 al 100

suma = 0

for numero1 in range (1, (100+1)):
    print(str(numero1))
    suma = suma + numero1
print("")
print("La suma total de los números es igual a: "+str(suma))
print(" ")

##Ejercicio 3 - Tabla de multiplicar

multiplicacion = 0
number_Usuario = int(input("Usuario introduce un número: "))
for numero2 in range (1, (10+1)):
    multiplicacion = numero2 * number_Usuario
    print("Tabla de multiplicar del número " +str(number_Usuario))
    print(str(number_Usuario)+ " x " +str(numero2)+ " = "  +str(multiplicacion))

print(" ")

##Ejercicio 4 - Números pares entre el 1 y el 50
print("Los números pares comprendidos entre el 1 y el 50 son: ")
for numero3 in range (1, (50+1)):
    if numero3 % 2 == 0 :
        print (str(numero3))
print(" ")   
    
##Ejercicio 5 - Factorial de un número

factorial = 1
print("Usuario, en este programa vamos a calcular el factorial de un número: ")
numberFactorial = int(input("Usuario, introduce un número: "))
for number in range (1, numberFactorial+1):
    factorial = factorial*number
print(str(factorial))
print(" ")
##Ejercicio 6 - Invertir una cadena
print("En este programa, vamos a invertir nuestra cadena: ")
cadena_invertida = " "
cadena = input("Usuario, introduce una cadena: ")

for letra in cadena :
    cadena_invertida = letra + cadena_invertida ##Para invertir, se tiene que poner este orden, primero la letra y luego la cadena/frase
print(cadena_invertida)
    
##Ejercicio 6 - Cadenas invertidas
print("En este ejercicio, vamos a invertir la cadena introducida por el usuario para construir una cadena invertida ")
frase = input("Usuario, introduce una frase ")
frase_invertida = " "

for letra in frase:
    frase_invertida =  letra +frase_invertida ##Para invertir, se tiene que poner este orden, primero la letra y luego la cadena/frase
print(frase_invertida)
print(" ")
##Ejercicio 7 - Contar vocales

print("En este programa, vamos a contar vocales ")
frase_prueba = input(" Usuario, dime una frase ")
vocales = "aeiouAEIOU"
contador_vocales = 0

for caracter1 in frase_prueba :
    if caracter1 in vocales:
        contador_vocales += 1
print("En total hay " +str(contador_vocales)+ " vocales en tu frase")
print(" ")

##Ejercicio 7 - Imprimir números primos hasta el número introducido por el usuario

def es_primo(n):
    if n < 0:
        return False
    if n ==2:
        return True
    if n%2 != 0:
        return True

print("En este programa se van a imprimir números primos, en donde podemos encontrarnos con: ")
number_Primo = int(input("Usuario, introduce un númerito: "))

for numero in range (1, number_Primo+1):
    if es_primo(numero):
        print(numero)

print(" ")       
##Ejercicio 8 - Cuadrados de una lista

cuadrados = []

for numero in range(1, 11):
    cuadrados = [numero**2]
    print(cuadrados)

##Ejercicio 9 - Cuadrados de una lista

cuadrados2 = []

for numero in range(1, 11):
    cuadrados2.append(numero**2)
    print(cuadrados2)

    
