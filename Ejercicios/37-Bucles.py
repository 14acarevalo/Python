## Ejercicio 1 - Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Usuario, introduce una palabra: ")

for ig in range (1, 11):
    print (f"{word}")
print("")
##Ejercicio 2 - Escribir un programa que pregunte la edad del usuario y muestre por pantalla todos los años que ha cumplido, desde 1 hasta su edad

edad = int(input("Usuario, cuantos años tienes: "))
print("Te mostraré por pantalla todos los años que has cumplido hasta el momento")
año = int(input("¿En que año naciste? "))

for number in range (1, edad+1):
    print(f"Has tenido {number} años en el año {año+number}")
print("")
##Ejercicio 3 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

number = int(input("Usuario, introduce un número: "))
for i in range (1, number+1):
    if i % 2 != 0:
        print(f"{i},")
        
##Ejercicio 4 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta el cero separado por comas

number = int(input("Usuario, introduce un número: "))
for i in range (number,-1,-1,):
    print(f"{i},") 
print("")
     
##Ejercicio 5 - Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión que dura cada año la inversión

cantidad = int(input("Usuario, ¿Cuanto vas a invertir? "))
interes = int (input("¿Qué interes anual vas a llevar a cabo? "))
años = int(input("¿Durante cuantos años? "))

for c in range (años):
    cantidad *= 1+interes/100
    print(f"La cantidad por año de {c} es de {cantidad}")
print("")
##Ejercicio 6 - Escribir un programa que muestre por pantalla la tabla de multiplicar del número al 10

print("Usuario, vamos a hacer la tabla de multiplicar de un número determinado: ")
numerito = int(input("Introduce un número: "))

for n in range (1, 10+1):
    multiplicacion = numerito * n
    print(f"La tabla de multiplicar del numero {numerito} x {n} es igual a {multiplicacion}")
print("")

##Ejercicio 7 - Escribir un programa que pida al usuario un número entero y muestre por pantalla un triangulo rectángulo como el de más abajo, de altura el número introducido

triangulo = int(input("Usuario, vamos a formar un triangulo, dime un número: "))

for i in range (triangulo):
    for j in range (i+1):
        print("*", end="")
    print("")
    
print("")

##Ejercicio 8 - Escribir un programa que almacene la cadena de caracteres CONTRASEÑA en una variable, pregunte al usuario por la contraseña hasta que introduzca la correcta

contraseña = "contraseña"

prueba = input("Usuario, introduce la contraseña: ")

while prueba != contraseña:
    print("Prueba otra vez: ")
    prueba = input("Introduce la contraseña: ")
    
print("Contraseña correcta!!!!")  

##Ejercicio 9 - Primo o no

number = int(input("Usuario, introduce un número y veremos si es o no primo: "))

while number % 2== 0:
    print(f"Lo siento, el número {number} no es primo")
    number = int (input("Introduce otro número: "))

print("Has introducido un número primo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")
##Ejercicio 11 - escribir palabras al revés

word = input("Usuario, introduce una palabra: ")

for i in range (1, len(word)):
    reversible = word [::-1]
    print(reversible)  
print("")   
##Ejercicio 12 - Escribir un programa que pregunte al usuario por una letra y una frase, ver las veces que se repiten 
frase = input("Usuario, introduce una frase: ")
letra = input("Usuario, que letra quieres tener en cuenta: ")
contador = 0

for i in frase:
    if i == letra:
        contador = contador +1
print(f"El número de veces que aparece la letra {letra} en la frase {frase} es igual a {contador}")