import math

#Ejercicio 1: Escribe un enunciado

print ("Este es el primer ejercicio para aprender pythton")
variable = "Voy a aprender este lenguaje con muchas ganas"
print (variable)
print (" ")

#Ejercicio 2: Realiza una suma

print ("Tengo varias formas de realizar dicha suma")
print ("Opcion a")
numero1 = 5
numero2 = 5
print ("La suma del numero " +str(numero1)+ " y del numero " +str(numero2)+ " es igual a: " +str((numero1+numero2)))
print(" ")
print("Opcion b")
numero3=5
numero4=5
suma= numero3+numero4
print ("La suma del numero " +str(numero3)+ " y del numero " +str(numero3)+ " es igual a: " +str(suma))
print(" ")

#Ejercicio3: Calcular el área de un rectángulo

lado = float(input("Usuario, introduce las dimensiones de un lado "))
anchura = float(input("Usuario, introduce las dimensiones del ancho "))
area = lado*anchura
print("El area de tu rectangulo es igual a " +str(area))
print(" ")

#Ejercicio 4: Conversor de temperaturas

celsius = float(input("Usuario, introduce la temperatura que marca tu termotro hoy "))
fahrenheit = celsius*32.25
print("La temperatura actual a fahrenheit son: " +str(fahrenheit)+ " grados")
print(" ")

#Ejercicio 5: Par o impar

numero = int(input("Usuario, introduce un numero "))
if numero % 2 == 0:
    print("El numero " +str(numero)+ " es par")
if numero % 2 != 0:
    print("El numero " +str(numero)+ " es impar")
print(" ")

#Ejercicio 6: contar numeros del 1 al 10

print("Usuario, vamos a contar numeros del 1 al 10")
for i in range(1, 11):
    print(i)
print(" ")

#Ejercicio 7: Tabla de multiplicar

print("Usuario, vamos a contar numeros del 1 al 10")
number = int(input("Usuario introduce un numero: "))
for i in range(1, 11):
    multiplicacion = number*i
    print("El resultado de multiplicar " +str(number)+ " x " +str(i)+ " es igual a " +str(multiplicacion) )
print(" ")

#Ejercicio 8: Encontrar el número más grande

num1 = int(input("Usuario, introduce un número "))
num2 = int(input("Usuario, introduce un segundo número "))
num3 = int(input("Usuario, introduce un tercer número "))

if num1 > num2 and num1 > num3:
    mayor = num1
if num2 > num1 and num2 > num3:
    mayor = num2
else: 
    mayor = num3
    
print ("El numero más grande es: " +str(mayor))




