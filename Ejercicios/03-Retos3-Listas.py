# 1. Suma de Elementos:
# Escribe una función que tome una lista de números y devuelva la suma de todos los elementos de la lista.
def suma_lista(lista):
    pass  # Implementa tu código aquí

list_1 = [1,2,3,4,5,6]
print(str(list_1))
sumaLista = sum(list_1)
print (str(sumaLista))

# 2. Promedio de Números:
# Escribe una función que tome una lista de números y devuelva el promedio.
def promedio_lista(lista):
    pass  # Implementa tu código aquí
list_2 = [1,2,3,4,5,6,7,8]
suma = sum(list_2)
totalLista = len(list_2)
promedioLista = sum(list_2) / len(list_2)
print("El resultado de este ejercicio 2, donde se nos pide el promedio queda: ")
print("La suma de la lista es igual a: " +str(suma))
print("El total de la lista es igual a: " +str(totalLista))
print("El promedio de la lista es igual al resultado de dividir la suma y el total de caracteres: " +str(promedioLista))

# 3. Números Pares:
# Escribe una función que tome una lista de números y devuelva una nueva lista con solo los números pares.

# 3. Números Pares:
# Escribe una función que tome una lista de números y devuelva una nueva lista con solo los números pares.

def numeros_pares(lista):
    pares = []  # Inicializa una lista vacía para almacenar los números pares
    for i in lista:  # Recorre cada número en la lista original
        if i % 2 == 0:  # Verifica si el número es par
            pares.append(i)  # Añade el número par a la lista 'pares'
    return pares  # Devuelve la lista de números pares

# Prueba de la función
list_par = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lista de prueba
print(numeros_pares(list_par))  # Salida esperada: [2, 4, 6, 8]


# 4. Eliminar Duplicados:
# Escribe una función que tome una lista y devuelva una nueva lista sin duplicados.


list_duplicados = ["a" , "b" , "c", "d", "e" , "a" , "b"]
contador = list_duplicados.count("a")
contador1 = list_duplicados.count("b")
contador2 = list_duplicados.count("c")
contador3 = list_duplicados.count("d")
contador4 = list_duplicados.count("e")

print(contador)
print(contador1)
print(contador2)
print(contador3)
print(contador4)

list_duplicados.remove("a")
list_duplicados.remove("b")
print(list_duplicados)


# 5. Producto de Elementos:
# Escribe una función que tome una lista de números y devuelva el producto de todos los elementos.
def producto_lista(lista):
    pass  # Implementa tu código aquí

# 6. Invertir Lista:
# Escribe una función que invierta una lista sin usar el método reverse() ni la sintaxis de rebanado [::-1].
def invertir_lista(lista):
    pass  # Implementa tu código aquí

# 7. Buscar Sublista:
# Escribe una función que tome dos listas y devuelva True si la segunda lista es una sublista de la primera, y False en caso contrario.
def es_sublista(lista, sublista):
    pass  # Implementa tu código aquí

# 8. Lista de Números Primos:
# Escribe una función que tome un número n y devuelva una lista de todos los números primos menores que n.
def numeros_primos(n):
    pass  # Implementa tu código aquí

# 9. Transponer una Matriz:
# Escribe una función que tome una matriz (lista de listas) y devuelva su transpuesta.
def transponer_matriz(matriz):
    pass  # Implementa tu código aquí
