#Ejercicio 1 - ValueError
#Escribe un programa que le pida al usuario que introduzca un número y lo convierta a un entero. 
#Si el usuario introduce algo que no se puede convertir a un número, muestra un mensaje de error.

try:
    number = int(input("Usuario, introduce un número entero: "))
    print(f"El número introducido es: {number}")
except ValueError:
    print("No has introducido un número entero")
    
#Ejercicio 2 - TypeError
#Crea una función que sume dos valores. 
#Si el usuario introduce valores que no sean números (enteros o flotantes), maneja el error adecuadamente.

def sumar(a,b):
    try:
        sumar = a + b
        print (f"El resultado es igual a {sumar} sumando {a} + {b}")
    except:
        print("Has introducido un valor mal, ambos tienen que ser número")

sumar(10,"a")

#Ejercicio 3 - ZeroDivisionError
#Escribe un programa que pida dos números e intente dividir el primero por el segundo. 
#Si el segundo número es 0, maneja la excepción ZeroDivisionError.

try:
    number1 = float(input("Usuario, introduce un número: "))
    number2 = float(input("Ahora introduce un segundo número:"))
    print(f"Los números introducidos son {number1} y {number2}")
    division = number1/number2
    print(f"El resultado es igual a {division}")
except ZeroDivisionError:
    print("no se puede dividir entre 0")
    
#Ejercicio 4 - ImportError
#Simula la importación de un módulo inexistente y maneja la excepción ImportError.

#try:
    #import modulo_falso
#except:
    #print("No has introducido ningún modulo original y verdadero")

#Ejercicio 5 - IndexError
#Crea una lista de 5 elementos y permite que el usuario acceda a uno de ellos introduciendo un índice. 
#Si el usuario introduce un índice fuera de rango, maneja el error adecuadamente.

my_list = [1,2,3,4,5,6,7,8,9,10]

try:
    introduction_number = int(input("Usuario, introduce un número entre el 1 y el 20: "))
    print(f"El valor {introduction_number} esta presente en {my_list(introduction_number)}")
except:
    print(f"Lo sentimos, tu número no está en la lista")
    





    
    