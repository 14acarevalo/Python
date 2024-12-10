##Ejercicio 1: Imprimir Números Pares
##Crea una función imprimir_pares que tome una lista de números y que imprima solo los números pares de la lista.

def num_Pares (list_numeros):
    for num in list_numeros:
        if num %2== 0:
            print(num)
            

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num_Pares(lista_de_numeros)
print(" ")


##Ejercicio 2: Sumar Elementos de una Lista
##Crea una función sumar_elementos que tome una lista de números y devuelva la suma de todos los elementos de la lista.

def sumar_elementos (list_numeros):
    return sum(list_numeros)

lista = [1,2,3,4,5,6]
resultado = sumar_elementos(lista)

print("El resultado de sumar todos y cada uno de los elementos de la lista, es igual a: " +str(resultado))

##Ejercicio 3: Contar Vocales en una Cadena
##Crea una función contar_vocales que tome una cadena de texto y devuelva el número de vocales (a, e, i, o, u) en la cadena.

def contar_vocales (list_vocales):
    return len(list_vocales)

lista_vocales = ["a" , "e", "i", "o" ,"u"]
vocales = contar_vocales(lista_vocales)
print("En total hay " +str(vocales)+ " vocales")
print(" ")
print("Creamos una variable para contar las vocales que hemos introducido en nuestra lista")

vocales = "aeiouAEIOU"

def contador_vocales (list_vocales):
    contador = 0
    for letra in list_vocales:
        if letra in vocales:
             contador += 1
    return contador

lista1_vocales = ["a" , "e", "i", "o" ,"u", "b", "f", "z"]

resultado = contador_vocales(lista1_vocales)
print("En total, en nuestra lista hay " +str(resultado)+ " vocales")

##Ejercicio 4: Encontrar el Máximo en una Lista
##Crea una función encontrar_maximo que tome una lista de números y devuelva el número más grande de la lista.

def encontrar_maximo (list_numeros):
    return max(list_numeros)

lista_numeros_maximo = [1,2,3,4,5,6,78, 8, 9]
maximo = encontrar_maximo (lista_numeros_maximo)
print("El número más grande de la lista, es igual a: " +str(maximo))

##Ejercicio 5: Verificar Palíndromo
##Crea una función es_palindromo que tome una cadena de texto y devuelva True si la cadena es un palíndromo (se lee igual de adelante hacia atrás) y False en caso contrario.


##Ejercicio 6: Factorial
## Crea una función calcular_factorial que tome un número entero y devuelva su factorial.

def calcular_factorial (list_numeros):
    factorial = 1
    for num in list_numeros:
        factorial = factorial * num    
    return factorial

list_numeros12 = [1,2,3,4]
resultado_factorial = calcular_factorial(list_numeros12)
print("El resultado del factorial de la lista que hemos obtenido, es igual a: " +str(resultado_factorial))

##Ejercicio 7: Contar palabras en una cadena
## Crea una función contar_palabras que tome una cadena de texto y devuelva el número de palabras en la cadena.

def contar_palabras (cadena_palabras):
    cadena_palabras.split()
    for palabra in cadena_palabras:
            palabra = cadena_palabras.split()
    return len(palabra)

cadena = "Hola ¿cómo estás señorito?"

contador_oficial = contar_palabras(cadena)
print("En total, en la frase hay " +str(contador_oficial)+ " palabras")

def contar (lista_palabritas):
    lista_palabritas.split()
    for palabras in lista_palabritas:
        palabras = lista_palabritas.split()
    return len(palabras)

cadena_texto = "Vamos con energia a por el lunes, ya falta menos para acabar"

total_palabras = contar(cadena_texto)
print("En total en esta frase, nos encontramos con :" +str(total_palabras)+ " palabras")

##Ejercicio 8: Verificar si un número es primo
##Crea una función es_primo que tome un número entero y devuelva True si el número es primo, y False en caso contrario.


def es_primo (lista_numeritos):
    for num in lista_numeritos:
        if num % 2 != 0 or num == 2 :
            return True
        else:
            return False
        
        
lista_numeros_primos = [8]
primos = es_primo(lista_numeros_primos)
print("El resultado para saber si el número es primo, es el siguiente: " +str(primos))
print(" ")

##Ejercicio 9: Mínimo en una lista
##Encuentra el número minimo de una lista determinada

def minimo_lista (numeros_lista):
    return min(numeros_lista)

lista_numeros_menor = [2,3,4,5,-1,9,20]

menor = minimo_lista(lista_numeros_menor)
print("El número más pequeño de la lista es el siguiente: " +str(menor))

##Ejercicio 10: Calcular el promedio de una lista
promedio = 0
suma= 0
def calcular_promedio (lista_numeros):
    for num in lista_numeros:
        suma = sum(lista_numeros)
        promedio = suma/len(lista_numeros)
    return promedio


lista_numeros_promedio = [1,2,3,4,5,6,7,8,9,10]
resultado_promedio = calcular_promedio (lista_numeros_promedio)
print("El promedio de la lista que hemos encontrado, es igual a: " +str(resultado_promedio))


##Ejercicio 11: Sacar numeros impares y pares

def numeros_pares_impares (lista_numeros):
        if num % 2 == 0:
            return "par"
        else:
            return "impar"


lista_numeros1 = [1,2,3,4,5,6,7,8,9,10]

for num in lista_numeros1:
    resultados = numeros_pares_impares(num)
    print("El numero " +str(num)+ " es: " +str(resultados))
    
##Ejercicio 12: Clasificar los números en pares, impares y 0

def clasificacion_numeros (lista_numeros):
    if num % 2 == 0 and num != 0:
        return " numero par"
    elif num % 2 != 0:
        return " numero impar"
    elif num == 0:
        return "el numero 0"
    else:
        return "El dato introducido no se asocia a ningún digito"


lista_personalizada = [1,2,3,4,5,6,7,8,9, 0, 12, 14, 0]

for num in lista_personalizada:
    resultados = clasificacion_numeros(num)
    print("El carecter y/o digito " +str(num)+ " se corresponde con " + resultados)

        