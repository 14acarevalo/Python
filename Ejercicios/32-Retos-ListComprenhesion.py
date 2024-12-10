print("Ejercicio 1 - Crear lista de cuadrados:")
listaCuadrados = [x**2 for x in range (1, 11)]
print("La lista de cuadrados que nos pide este ejercicio, con rango 1 - 10, es igual a: " +str(listaCuadrados))
print(" ")

print("Ejercicio 2 - numeros pares del 1 al 20:")
listaPares = [par for par in range(1, 21) if par %2 == 0]
print("Los números pares del intervalo del 1 al 20, es igual a: " +str(listaPares))
print(" ")

print("Ejercicio 3 - primeras letras")
palabras = ["manzana" , "banana" , "pera", "uva"]
print(palabras)
primerasLetras = [letra[0] for letra in palabras]
print("La primera letra de la lista palabras, es igual a: " +str(primerasLetras))
print(" ")

print("Ejercicio 4 - numeros divisibles por 3")
divisiblesX3 = [numero for numero in range (1, 21) if numero%3==0]
print("Los números divisibles x 3, de una lista del 1 al 20, son: " +str(divisiblesX3))
print(" ")

print("Ejercicio 5 - Sacar lista con los cubos de los números impares")
cubosImpares = [numerito**3 for numerito in range (1, 11) if numerito %2 != 0]
print("Los cubos impares de una lista, comprendida entre 1 y 10, es igual a: " +str(cubosImpares))
print(" ")

print("Ejercicio 6 - Multiplica pares e impares")
multiplicacion = [numero*2 if numero %2== 0 else numero*3 for numero in range(0, 11)]
print("En este apartado, se multiplican los números en función de si son pares, por 2, o impares, por 3: " +str(multiplicacion))

print("Ejercio 7 - Palabras de longitud par")
listaPalabras = ["casa", "perro" , "gato" , "elefante" , "raton"]
print(listaPalabras)
sacarPalabrasPares = [letra for letra in listaPalabras if len(letra) %2 == 0]
print("Las palabras pares de la lista anterior son: " +str(sacarPalabrasPares))
print(" ")

print("Ejercicio 8 - Numeros por intervalso")
numerosIntervalos = [(x, y) for x in range(1, 3) if x%2==0 for y in range(4, 6)  if y%2==0]
print("Sacando numeros por intervalos, obtenemos: " +str(numerosIntervalos))

print("Ejercicio 9 - Diccionario con longitud de palabras ")
palabras2 = ["manzana" , "banana" , "pera", "uva"]
print(palabras2)
listadoLetras = [len(palabra) for palabra in palabras2]
print("La longitud de las diferentes palabras de la lista es: "+str(listadoLetras))

