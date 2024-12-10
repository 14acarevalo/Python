#Nos vamos a encontrar con diferentes retos para seguir aprendiendo python

#Reto1: Escribir una palabra y que se cuente los carácteres que tiene
palabra = input("Usuario, introduce una palabra: ")
longitud = len(palabra)
print ("La palabra " +str(palabra)+ " tiene un total de " +str(longitud)+ " caracteres")
print (" ")

#Reto2:Contar numeros pares
num = int(input("Usuario, introduce un numero y contaremos los pares que hay dentro de este: "))
for i in range (1, num +1):
    if i % 2 == 0:
        print("El numero " +str(i)+ " es par")
    else: 
        print("El numero " +str(i)+ " es IMpar")
        
#Reto3: Programa que sume todos los números pares de un intervalo
print ("Vamos a sumar todos los numeros del 1 al 100 pares")
suma = 0
for i in range (1, 101):
    if i % 2 == 0:
        print("El numero " +str(i)+ " es par")
        suma += i
    else:
        print("El numero " +str(i)+ " es impar")
print (" ")
print("La suma de los numeros pares es: " +str(suma))
print (" ")

#Reto4: Escribir los 10 primeros numeros y su cuadrado
print("Vamos a sacar los 10 primeros números y su cuadrado")
for i in range (1, 11):
    cuadrado = i*i
    print("El numero es: " +str(i))
    print("El cuadrado es: " +str(cuadrado))
    print(" ")
    
#Reto5: Calcular el factorial de los números
print("Vamos a calcular el factorial")
number = int(input("Usuario, introduce un numero: "))
factorial = 1
for i in range (1, number):
    factorial=factorial*i
    print("El factorial del número " +str(number)+ " es igual a " +str(factorial))
    print(" ")
    
#Reto6: Encontrar los numeros primos dentro de un rango
print("Usuario, vamos a buscar los números primos dentro de un rango ")
numPrimo = int(input("Usuario, introduce un número: "))
contadorPrimo = 0
for i in range (1, numPrimo + 1):
    if numPrimo <= 1:
        if i % 2 != 0 or i/1 == i or i == 2:
            print("El número " +str(i)+ " es primo")
        contadorPrimo+=1
    else:
        print("El número " +str(i)+ " no es primo")
        
print ("En total hay " +str(contadorPrimo)+ " numeros primos")
print(" ")

#Reto7: Determinar si un numero es positivo, negativo o es igual a 0
num1 = int (input("Usuario, introduce un numero: "))
if num1  <0:
    print("El numero es número negativo")
if num1  == 0:
    print("El numero es igual a 0")
if num1  >0:
    print("El numero es igual a número positivo")
print(" ")

#Reto8: ¿Año bisiesto?
año = int(input("Usuario, introduce un año: "))
if (año % 4 == 0 and año%100 !=0) or año%400 == 0:
    print("El año " +str(año)+ " es bisiesto")
else:
    print("El año " +str(año)+ " no es bisiesto")
print(" ")

#Reto9: Calcula el descuento sobre el precio original
precio = float(input("Usuario, cuanto te ha costado tu producto: "))
rebaja = 10
precioDescuento = (precio*rebaja)/100
precioFinal = (precio-precioDescuento)
print("El descuento de tu producto cuyo precio original era " +str(precio)+ " €, es con el descuento del 10%: " +str(precioFinal)+ " €")
print(" ")

#Reto10: Calcula el descuento solo si la compra es superior a 100 €
precioProducto = float(input("Usuario, cuanto te costó tu producto nuevo: "))
if precioProducto > 100:
    rebaja2 = 10
    precioDescuento2 = (precioProducto*rebaja2)/100
    precioFinal2 = (precioProducto-precioDescuento2)
    print("El descuento de tu producto cuyo precio original era " +str(precioProducto)+ " €, es con el descuento del 10%: " +str(precioFinal2)+ " €")
else:
    print("Tu producto no tiene descuento y por lo tanto, su precio es el mismo: " +str(precioProducto)+ " €")      
    print(" ")
    
#Reto11: Determinar el estado del agua
temperatura = float(input("Usuario, mira el termómetro y dime a que temperatura está el agua: "))
if temperatura < 0:
    print("Es sólido, estamos hablando de hielo")
if temperatura <= 100 and temperatura > 0:
    print("El agua es líquida, estamos hablando de agua")  
else:
    print("Es gaseosa, estamos hablando de gas") 
