##Ejercicio 1. Generador de tabla de mulitpolicar en una función

def multiply_table(number):
    """
    En esta funcion se busca crear una tabla de multiplicar

    Args:
        (number) que será el dígito que el usuario introduzca para la tabla de multiplicar
        
    Resultado:
    Una operación matematica, teniendo en cuenta el intervalo del 1 al 10, al usar el bucle for y el número multiplicado
    """
    
    for i in range (1, 11):
        multiply = i*number
        print(f"El numero {i} multiplicado por {number} es igual a: {multiply}")

number1 = int(input("Usuario, introduce un número: "))

multiplication = multiply_table(number1)
print(multiplication)
print(" ")

##Ejercicio 2. Simulador de varias operaciones:

def operation1(x, y, operation ="add"):
    """
    Función para realizar varias operaciones

    Args:
        (x, y, operation ="add") a través de los cuales se identifica las variables númericas y además según el tipo string la operacion

    Returns:
        Una operación matemática según los digitos introducidos y la palabra add, mul, div o rest que llevará a cabo la operación matemática
    """
    if operation == "add":
        result = x+y
    elif operation == "rest":
        result = x-y
    elif operation == "multi":
        result = x*y
    elif operation == "div":
        if x>y:
            result = x/y
        else:
            return "No se puede llevar a cabo la operacion porque el segundo digito es mayor que el primero"
    return result

number1 = int(input("Usuario, introduce un número: "))
number2 = int(input("Usuario, introduce el segundo número: "))
palabra = (input("Usuario, introduce la acción: (add para sumar) ,(rest para restar), (multi para multiplicar) o (div para dividir): ")) 

print(operation1(number1, number2, palabra))
print(f"El resultado de la combinación de los digitos {number1} y {number2} y la palabra {palabra} trae consigo: {operation1(number1,number2, palabra)}")
print(" ")

##Ejercicio 3, Números primos:

def es_primo(number):
    """
    Función para identificar numeros primos

    Args:
    (Number) se introducirá un número elegido por el usuario para saber si es o no primo

    Returns:
    En función de si el número es 1, 2 o divisible por impares nos dara un número impar o par. 
    """
    if number == 2 or number % 2 != 0 or number == 1 :
        return "Es primo"
    else:
        return "No es primo"
        
cousin_number = int(input("Usuario, introduce un número: "))
result = es_primo(cousin_number)
print(f"El número introducido, {cousin_number} es: {result}")
print("")
##Ejercicio 4, Funcion para sumar números pares: 

def suma_pares(numero):
    """
    Funcion para números pares
    
    Args:
    (numero) que será el introducido por el usuario para establecer el rango de amplitud a considerar de cara a la suma de los números pares
    
    Returns:
    Sumatorio de los números pares y su resultado

    """
    suma = 0
    for number in range (1,numero+1):
        if number % 2 == 0:
            suma = suma + number
    return suma


digito = int(input("Usuario, introduce el número tope que quieres realizar la suma: "))
resultado = suma_pares(digito)
print(f"El resultado, sumando solamente los números pares, es igual a: {resultado}")
print("")
        
#Ejercicio 5: Adivina el numero
import random

def guess_number(secret_number, magic_number):
    """
    Funcion para adivinar el numero

    Args:
        secret_number (_type_): Es el número secreto de tipo int random
        magic_number (_type_): Es el número que el usuario va a introducir
        
    Return:
    El resultado dependerá de si el usuario acierta, se aproxima o introduce un número superior/inferior al establecido
    """

    if magic_number == secret_number:
        print("Premio!! Has acertado!!!")
        return True
    
    elif magic_number > secret_number:
        print("El número introducido no es el correcto, es más grande!!!!! ")
    
    else:
        print("El número introducido no es el correcto, es más pequeño!!!!! ")
    return False

secret_number = random.randint(1,14)


print("Usuario, adivina el número secreto... ")

magic_number = int(input("Usuario, introduce un número: "))
acertado = guess_number(secret_number, magic_number)

acertado = False
while not acertado:
    print("El resultado no es el correcto y por lo tanto el número introducido no es el deseado...")
    magic_number = int(input("Usuario, introduce un número de nuevo: "))
    acertado = guess_number(secret_number, magic_number)

print("Has acertado!!!!!!")
print("")
#Ejercicio 6: Contador de vocales

def count_char(palabra):
    """
    Función para contar vocales

    Args:
        palabra (_type_): Caracter de tipo string introducida por el usuario

    Returns:
        El numero total de vocales de la palabra
    """
    vocales="aeiouAEIOU"
    contador = 0
    
    for char in palabra:
        if char in vocales:
            contador +=1
    return contador

word = input("Usuario, introduce una palabra: ")
result = count_char(word)
print(result)
print("")
        
#Ejercicio 7: Números perfectos

##Un número perfecto es aquel que es igual a la suma de sus divisores


    

    
##Ejercicio 8: Invertir una cadena

def invertir_cadena (cadena):
    palabra = ""
    for char in cadena:
        palabra = char+palabra
    return palabra

word = input("Usuario, introduce una palabra: ")
result = invertir_cadena(word)
print(f"El resultado de invertir la terminologia de tu palabra, es igual a: {result}")
print("")

##Ejercicio 9: Factorial de un número
def factorial (number):
    factorial = 1
    for num in range (1, number):
        factorial = factorial*num
    return factorial

numero = int(input("Usuario, introduce un número: "))
resultado = factorial(numero)
print(f"El factorial del número {numero} es igual a {resultado}")
print("")
##Ejercicio 9: Contar múltiplos de 3 y de 5

def contador_multiplos(number):
    """Contador de multiplos

    Args:
        number (_type_): Valor de tipo numerico (int) con el objetivo de introducir un número
        En función de si el número es divisible por 3, 5 o ambos, saldrá un contador y/o numero del intervalo que establezca el usuario desde 
        el 1 al número que este introduzca

    Returns:
    Los números que hay divisibles por 3, 5 o ambos en dicho intervalo
        
    """
    contador3=0
    contador5=0
    contador3y5=0
    for num in range (1, number+1):
        if num % 3 == 0:
            contador3+= 1
        elif num % 5 == 0:
            contador5+= 1
        elif num %3 and num%5 == 0:
            contador3y5+=1
    return (
        f"-Multiplos en total de 3: {contador3} - Multiplos en total de 5: {contador5} - Multiplos en total de ambos: {contador3y5}")
        
numberPlayer = int(input("Usuario, introduce un número: "))
resultado = contador_multiplos(numberPlayer)
print(f"Nos encontramos con: {resultado}")
print("")

##Ejercicio 10 Mayor y menor

def mayor_menor(numero):
    """Función mayor y menor

    Args:
        numero (_type_): Valor númerico que introducirá el usuario para establecer el rango del intervalo

    Returns:
        Devolverá el número más pequeño, que siempre será 1 al ser el valor del intervalo mínimo
        y el número introducido, ya que será siempre el más grande
        Nos devuelve dos valores de tipo int, mayor y menor.
    """
    mayor = 0
    menor = numero
    for num in range(1, numero + 1):
        if mayor < num:
            mayor = num
        if menor > num:
            menor = num
    
    return {f"El número mayor es: {mayor} y el numero menor es: {menor}"}

print ("Usuario, estable vamos a buscar el número menor y mayor de tu intervalo de números: ")
number = int(input("Introduce el número que medirá el rango: "))
resultado = mayor_menor(number)
print(resultado)
print("")

#Ejercicio 11 Mayor y menor 2.0

def numeroMayor_numeroMenor(num, num1):
    mayor = num1
    menor = num
    if num1 < num:
        mayor = num
        menor = num1
    else:
        menor = num
        mayor = num1
    
    return f"El número mayor es {mayor}, el número menor es {menor}"
        
        
numero = int(input("Usuario, introduce un número: "))
numero1 = int(input("Usuario introduce otro número: "))
resultado_final = numeroMayor_numeroMenor(numero, numero1)
print(f"Nos encontramos con: {resultado_final}")
   


            
        