##Ejercicios set

##Ejercicio 1: Unión de Conjuntos - Crea dos conjuntos y encuentra su unión.
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,10,11}
print(set_1.union(set_2))
print(" ")

## Ejercicio 2: Intersección de Conjuntos - Crea dos conjuntos y encuentra su intersección.
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,10,11}
print(set_1.intersection(set_2)) ##Sale set() porque no hay ninguno en común
print(" ") 
set_3 = {1,2,3,4,5,6,7}
set_4 = {7,8,9,10,11}
print(set_3.intersection(set_4)) ##Sale 7
print(" ")

##Ejercicios dict

## Ejercicio 1: Creación y Acceso - Crea un diccionario con al menos tres pares clave-valor y accede a uno de los valores.

dict_1 = {"Alberto" : 1, "Pablo" : 2, "Mama" : 3, "Papa" : 4}
print(dict_1)

## Ejercicio 2: Actualización de Valores - Actualiza uno de los valores en el diccionario.
dict_1 = {"Alberto" : 1, "Pablo" : 2, "Mama" : 3, "Papa" : 4}
dict_1 ["Alberto"] = 5
print(dict_1)

## Ejercicio 3: Eliminación de Pares Clave-Valor - Elimina un par clave-valor del diccionario.
dict_2 = {"Nombre" : "Alberto" , "Edad" : 30, "Estado" : "en una relacion"}
print(dict_2)
del dict_2 ["Edad"]
print(dict_2)

## Ejercicio 4: Iteración sobre un Diccionario -Itera sobre un diccionario e imprime sus claves y valores.

iterador = iter(dict_1)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

## Ejercicio 5: Uso del Método get - Utiliza el método get para acceder a un valor en el diccionario sin causar un error si la clave no existe.

dict_3 = {"Nombre" : "Alberto" , "Edad" : 30, "Estado" : "en una relacion"}
ciudad = dict_3.get("Ciudad" , "desconocida")
print(dict_3)
