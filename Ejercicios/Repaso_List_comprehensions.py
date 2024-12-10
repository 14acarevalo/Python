##Repaso de las lists comprehension:

print ("Ejercicio 1: ")
print ("En este ejercicio, lo que vamos a trabajar es el cubo de determinados números en rango del 1 al 10: ")

cubo = [x**2 for x in range (1,11)]
print("Los cuadrados de los números del 1 al 10, son: ")
print(cubo)
print("")

print("Ejercicio 2: ")
print("En este ejercicio, vamos a crear una lista que contenga sólo las vocales de la palabra pythonist ")
vocales = ["a", "e", "i", "o", "u"]
palabra = "pythonist"

vocal = [letra for letra in palabra if letra in vocales]
print(vocal)
print("")

print("Ejercicio 3: ")
print ("Números impares de una lista determinada: ")
impar = [1,2,3,4,5,6,7,8,9,10,11]
numero = [x for x in impar if x % 2 != 0]
print ("Los números impares que hemos conseguido son los siguientes: ")
print (numero)
print("")

print ("Ejercicio 4: ")
print("En este ejercicio vamos a generar una tupla con numeros y cuadrados ")
lista = [(x, x**2) for x in range (1,6)]
print("La lista con las tuplas queda asi: ")
print (lista)
print("")

print("Ejercicio 5: ")
number = [1,2,3]
lyst = ["a","b","c"]
print(f"Lista 1: {number} y de la lista 2: {lyst}")

combination = [(x,y) for x in number for y in lyst]
print("La combinación de ambas listas, queda asi: ")
print(combination)

print ("Ejercicio 6: ")
print("Vamos a sacar la longitud de las diferentes palabras de una lista determinada: ")
words = ["python", "list","comprehension", "ejercicios"]
print (f"La lista es: {words}")
longitud_palabras = [len(x) for x in words]
print("La longitud de las palabras es: ")
print(longitud_palabras)
print("")
print("Ejercicio 7: ")
print("Vamos a sacar los números divisibles por 3 y por 5 en un rango del 1 al 50")
divisibles = [x for x in range (1,51) if x % 3 == 0 or x % 5 == 0]
print("Los números divisibles que podemos encontrarnos son: ")
print(divisibles)
print("")

print("Ejercicio 8: ")
print ("En este ejercicio, hay una serie de palabras y tenemos que sacar en la nueva lista, todas aquellas con más de 5 caracteres ")
words_lyst = ["ordenador", "móvil", "ratón", "pantalla", "cable", "teclado", "silla"]
nueva_lista = [palabra for palabra in words_lyst if len(palabra)>5]
print("La nueva lista actualizada queda asi: ")
print(nueva_lista)
print("")

print("Ejercicio 9: ")
print("En este ejercicio vamos a generar una lista con números primos del 1 al 50")
numeros_primos = [x for x in range (1,51) if x % 2 != 0 or x <= 2]
print("Los números primos que podemos encontrarnos del 1 al 50 son: ")
print(numeros_primos)
print("")

print("Ejercicio 10: ")
print("En este ejercicio, vamos a realizar un filtrado de una sublista inicial: ")
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print("La lista es la siguiente: ")
print(matriz)

par = [x for sublista in matriz for x in sublista if x % 2 == 0] #Aplicamos el doble filtrado
print("El filtrado de lista con número par es igual a: ")
print(par)
print("")

print("Ejercicio 11: ")
print("En este ejercicio, vamos a realizar multiples sumas para un rango determinado ")

lista_10 = [1,2,3,4,5,6,7,8,9,10]
suma_lista = 0 
suma_lista = sum(lista_10)
print (suma_lista)

numeros = (1,11)

sumatorio = [sum(range(1,x+1)) for x in numeros ]
print ("El sumatorio total queda asi: ")
print(sumatorio)
print(" ")

print("Ejercicio 12: ")
print("Vamos a realizar un producto acumulado: ")
lista_numeros = range(1,11)
producto = [range(1, i*(i+1)) for i in lista_numeros]
print("El resultado es: ")
print(producto)

print("Ejercicio 13: ")
print("Vamos a realizar una suma acumulada de productos pares")
numeros_pares =  range(1,20)

sumatorio_numeros_pares = [sum(range(2, x+1)) for x in numeros_pares if x % 2 == 0]
sumatorio_numeros_pares = [suma_acumulada := suma_acumulada + x for x in numeros_pares if x % 2 == 0]

print("El listado queda asi: ")
print(sumatorio_numeros_pares)

print("Ejercicio 13: ")
print("Vamos a realizar una suma acumulada de números pares")

numeros_pares = range(1, 21)  # Asegurémonos de incluir el 20
suma_acumulada = 0

# List comprehension para la suma acumulada de números pares
sumatorio_numeros_pares = []
for x in numeros_pares:
    if x % 2 == 0:
        suma_acumulada += x
        sumatorio_numeros_pares.append(suma_acumulada)

print("El listado queda así: ")
print(sumatorio_numeros_pares)

