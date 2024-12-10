##En este reto, vamos a realizar varios ejercicios a modo de examen con el fin de seguir practicando y mejorando:

print("Ejercicio 1 - Sumar números básicos")
print("En este ejercicio, vamos a sumar dos números que nos de el usuario")
numero = int(input("Usuario, introduce un primer número: "))
numero1 = int(input("Usuario, introduce un segundo número: "))
suma = numero + numero1
print(f"El resultado de todas estas operaciones es igual a {suma}")
print(" ")

################################################################################
print("Ejercicio 2 - Número par o impar ")
print("En este programa se pide descubrir si el número es par o impar")
numero3 = int(input("Usuario, dame un número: "))
if numero3 % 2 == 0:
    print(f"El numero {numero3} es par")
else:
    print(f"El numero {numero3} es impar")
print("")

################################################################################
print("Ejercicio 3 - Contar Vocales")
print("En este ejercicio vamos a llevar a cabo la cuenta de las diferentes vocales de una palabra: ")
vocal = "aeiouAEIOU"
contadorVocales = 0

palabra = input("Usuario, introduce una palabra: ")
for letra in palabra:
    if letra in vocal:
        contadorVocales +=1
print(f"En la palabra {palabra} hay un total de {contadorVocales}")
print(" ")

################################################################################
print("Ejercicio 4 - Fibonacci")
print("En este programa lo que vamos a realizar es la opción fibonacci")
numero4 = int(input("Usuario, introduce un número: "))
fibonacci = 0
for num in range (1, (numero4+1)):
    fibonacci = fibonacci + num
    print (str(fibonacci))

###############################################################################
print("Ejercicio 5 - Ordenación de números")
print("En este programa, lo que vamos a realizar es la ordenación de una lista de números ")
lista = [2,5,1,6,3,4]
lista.sort()
print(lista)
print(" ")

###############################################################################
print("Ejercicio 6 - Palindromo")
print("Un palindromo, es una palabra que se escribe igual de un lado al otro")
palabra1 = input("Usuario, introduce una palabra: ")
def palindromo (palabra):
    return palabra == palabra[::-1]

if palindromo(palabra1):
    print("Nos encontramos ante un palindromo")
else:
    print("La palabra introducida no es un palindromo")
print(" ")

###############################################################################
print("Ejercicio 7 - Calcular el factorial")
print("En este programa vamos a realizar el calculo factorial de una serie de números: ")
numeroFactorial = int(input("Usuario, por favor, introduce un número entero que no sea 0: "))
def calcularFactorial (numero):
    factorial = 1
    if numero>0:
        for number in range(1, numero+1):
            factorial = factorial * number
        return factorial

print ("El factorial es igual a " +str(calcularFactorial(numeroFactorial)))
print(" ")
###############################################################################

print("Ejercicio 8 - Vamos a trabajar con funciones y conversiones de temperatura")

def conversionKelvinFahereint(temperatura1, grados):
    return temperatura1 == (grados * 9/5)+32

def conversionFahereintKevil(temperatura2, grados) :
    return temperatura2 == grados +273.15

print("Usuario, en este ejercicio, vamos a convertir la temperatura de kelvin a fahereint: ")
grados1 = int(input("Introduce los grados que deseas convertir: "))
resultadosConversor = conversionFahereintKevil(grados1)
print("El resultado es igual a " +str(resultadosConversor))
    

    


    

