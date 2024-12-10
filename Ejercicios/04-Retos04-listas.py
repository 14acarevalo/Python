# 1. Contar Elementos:
# Escribe una función que tome una lista y devuelva el número de elementos en la lista.
def contar_elementos(lista):
    return len (lista)

list_elementos = [1,2,3,4,5,6,7,8]
print(contar_elementos(list_elementos))
print(" ")

## Ejercicio 1: Imprimir el Número de Elementos en una Lista
imprimir_numeros = [1,2,3,4,5,6,7,8,9]
print(len(imprimir_numeros))
print(" ")

## Ejercicio 2: Imprimir la Suma de los Elementos en una Lista
print(sum(imprimir_numeros))
print(" ")

## Ejercicio 3: Imprimir el Elemento Máximo de una Lista
print(max(imprimir_numeros))

##Ejercicio 4: Imprimir el Elemento Mínimo de una Lista
print(min(imprimir_numeros))
print(" ")

## Ejercicio 5: Imprimir una Lista en Orden Inverso
print(imprimir_numeros[::-1])
print(" ")

## Ejercicio 6: Comprobar si un Elemento está en una Lista e Imprimir el Resultado
print(imprimir_numeros.count(3))
print(imprimir_numeros.count(100))
print(4 in imprimir_numeros) ##Esto es otra forma de hacerlo
print(" ")

## Ejercicio 7: Eliminar un Elemento de una Lista e Imprimir la Lista Resultante
delete_number = [1,2,3,4,5,6,7,8]
delete_number.remove (3)
print(str(delete_number))
print(" ")

## Ejercicio 8: Encontrar la Posición de un Elemento en una Lista e Imprimir la Posición
print(imprimir_numeros.index(2))
print(" ")

## Ejercicio 9:. Filtrar Números Pares y Ordenar:
# Escribe un programa que tome una lista de números, filtre solo los números pares,
# y devuelva una nueva lista con los números pares ordenados en orden ascendente.
print("Vamos a complicar algo más los ejercicios ")
print(" ")

list_numeros = [12,22,24, 8, 1,2,3,4,5,6,7,9,10]
for numero in list_numeros :
    if numero % 2 == 0:
        print (str(numero))
print(" ")
      

 ## Ejercicio 10: Crear una Lista de Cadenas en Mayúsculas
nombres =  ["alberto" , "rodolfo" , "pepe"]
mayusculas = [nombres.upper() for nombres in nombres]
print(mayusculas)
print(" ")

## Ejercicio 11a: Contar la Frecuencia de Cada Elemento en una Lista
list_contar = ["a", "b", "c", "d", "e", "f", "g"]
contador = list_contar.count("a")
contador1 = list_contar.count("b")
contador2 = list_contar.count("c")
contador3 = list_contar.count("d")
contador4 = list_contar.count("e")
contador5 = list_contar.count("f")
contador6 = list_contar.count("g")

print("La letra a se repite: "+str(contador)+ "\nLa letra b se repite: "+str(contador1)+ "\nLa letra c se repite: "+str(contador2)+ "\nLa letra c se repite: "+str(contador2)+ "\nLa letra d se repite: "+str(contador3)+ "\nLa letra e se repite: "+str(contador4)+ "\nLa letra f se repite: "+str(contador5)+ "\nLa letra g se repite: "+str(contador6))
print(" ")

# Ejercicio 11b. Contar la Frecuencia de Cada Elemento:
# Escribe un programa que tome una lista de elementos y devuelva un diccionario que muestre la frecuencia de cada elemento en la lista.

list_frecuencia = [1,2,3,4,5,5,6,8,9,1,2,3,5,6,7,8]
frecuencias = {}

for numero in list_frecuencia:
    if numero in frecuencias:
        frecuencias [numero] += 1
    else :
        frecuencias[numero] = 1

print(frecuencias)
print(" ")

    
## Ejercicio 12: Generar una Lista de Números en un Rango Específico
list_rango = [1,2,3,4,5, 10, 11, 14, 20, 7, 5, 4, 3, 17, 2, 15]
rango = [] ##Utilizamos estos corchetes porque es una lista, no un diccionario
for numero in list_rango :
    if numero >= 10 and numero <=20 :
        rango.append(numero)
print(str(rango))
print(" ")

        
## Ejercicio 13: Sumar Elementos de una Lista
list_sumar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(str(sum(list_sumar)))
print(" ")

   
## Ejercicio 14: Encontrar el Número Máximo y Mínimo
list_buscar = [-1,-21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,100]
print("El número más grande de la lista es: ")
print(str(max(list_buscar)))
print("El número más pequeño de la lista es: ")
print(str(min(list_buscar)))
print(" ")


## Ejercicio 15: Eliminar Elementos de una Lista
list_eliminar = [-1,-21,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,100]
eliminar = []
for numero in list_eliminar:
    if numero >= 10 and numero <= 20 :
        eliminar.append(numero)
print(eliminar)
print(" ")


## Ejercicio 16: Concatenar Listas de Números Pares y Números Impares
list_par = [2,4,6,8,10]
list_impar = [1,3,5,7,9]
list_total = [str(list_par) + " concatemamos con: " +str(list_impar)]
print(list_total)
list_concatenar = list_par + list_impar
print(list_concatenar)
print(" ")


## Ejercicio 18: Invertir una lista
list_invertir = [ "a", "b", "c", "d", "e", "f", "g", "h","i"]
invertir = list_invertir [::-1]
print(invertir)
print(" ")


## Ejercicio 19: Multiplicar Elementos por un Factor
print("Vamos a realizar una multiplicación, atento: ")
print(" ")

list_multi = [1,2,3,4,5,6,7,8,9]
numero3 = 3
multiplicacion = [numero*numero3 for numero in list_multi]
print(multiplicacion)
print(" ")

## Ejercicio 20: Filtrar Palabras que Empiezan con una Letra Específica
list_palabras = ["alberto" , "salario", "amar" , "leer" , "deporte", "ganar"]
letra = "a"
encontrar_letra = [palabra for palabra in list_palabras if palabra.startswith(letra)]                                                           
print(encontrar_letra)
print(" ")

## Ejercicio 21: Sumar los Elementos de una Lista
list_number1 = [1,2,3,4,5]
print(str(sum(list_number1)))

## Ejercicio 22: Crear una Lista de Cuadrados de Números
list_cuadrados = [1,2,3,4,5,6]
cuadrado = [numero **2 for numero in list_cuadrados]
print(str(cuadrado))
print(" ")

## Ejercicio 23: Contar Palabras en una Frase
list_palabras = "En esta frase vamos a extendernos para ver si cuenta las letras"
palabras = list_palabras.split()
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] +=1
    else :
       frecuencia_palabras[palabra] =1

print(frecuencia_palabras)
print(" ")

## Ejercicio 29: Reemplazar Elementos en una Lista

list_numeros = [1,2,3,4,5,6,1,1,1,1]
cambio = [99 if numero == 1 else numero for numero in list_numeros]
print(str(cambio))
print(" ")

## Ejercicio 30: Encontrar Elementos Comunes en Dos Listas
lista1_number = [1,2,3,4,5,6,7,8]
lista2_number = [5,2,7,9,10,11,1]

comun = [numero for numero in lista1_number if numero in lista2_number ]
print(str(comun))