#Repaso de listas y los diferentes comandos para ponerlos en práctica una vez más
print("Ejercicio 1: ")
#Crea una lista vacía y pide al usuario que ingrese 5 números. 
#Usa el método append() para añadir cada número a la lista y luego imprime la lista final.
numeros = []
print("Usuario, introduce 5 números: ")
for i in range (5):
    numero = int(input(f"Usuario, ingresa el número {i+1}: "))
    numeros.append(numero)

print(f"La lista definitiva queda asi: {numeros}")
print("")

print("Ejercicio 2: ")
#Dada la lista mi_lista = [1, 2, 3] y otra lista nueva_lista = [4, 5, 6], 
# usa el método extend() para combinar ambas listas y luego imprime el resultado.
mi_lista = [1, 2, 3]
nueva_lista = [4, 5, 6]
print(f"Lista 1: {mi_lista}")
print(f"Lista 2: {nueva_lista}")

mi_lista.extend(nueva_lista)
print(f"Tras concatenar las dos listas, nos encontramos: {mi_lista}")
print("")

print("Ejercicio 3: ")
#Tienes la lista mi_lista = [10, 20, 30, 40]. 
# Usa el método insert() para agregar el número 25 entre el 20 y el 30. Imprime la lista resultante.

number_list = [10, 20, 30, 40]
print (f"Lista original {number_list}")
number_list.insert(2, 25)
print(f"El resultado de añadir el 25 en la posición 2, es de: {number_list}")
print("")

print("Ejercicio 4: ")
#Dada la lista mi_lista = [5, 10, 15, 10, 20], 
# usa el método remove() para eliminar la primera aparición del número 10 y luego imprime la lista.

remove_list = [5,10,14,14,2,5,10,6,78,10]
print(f"Lista original: {remove_list}")

remove_list.remove(14)
print(f"Si le añado un número, en este caso 14, me eliminará el primer número que se corresponda con 14: {remove_list}")
print("")

print("Ejercicio 5: ")
#Dada la lista mi_lista = [10, 20, 30, 40, 50], 
# elimina el último elemento usando pop() y muestra el valor eliminado y la lista resultante. 
# Luego, elimina el elemento en la posición 1 y vuelve a imprimir la lista.

lyst = [10, 20, 30, 40, 50]
print(f"Lista que nos encontramos para trabajar en este ejercicio: {lyst}")
ultimo_elemento = lyst.pop()
print(f"Número eliminado: {ultimo_elemento}")
print(f"Lista definitiva: {lyst}")
print("Ahora, vamos a eliminar el elemento de la posición 1: ")
primer_elemento = lyst.pop(1)
print(f"Número eliminado: {primer_elemento}")
print(f"Lista definitiva: {lyst}")
print("")

print("Ejercicio 6: ")
#Crea una lista con algunos elementos, luego usa el método clear() para vaciarla completamente y verifica que la lista esté vacía imprimiéndola.
# Aprovecha antes y cuenta cuantas veces aparece un número determinado, el que te de la gana con count()
lista_creada = [1,2,3,4,5,6,7,8,9,3,4,5,67,4,5,6,3,4,6]
print(f"Lista: {lista_creada}")

print(f"Lista con contador de un número al azar, el 4: {lista_creada.count(4)} veces aparece")
lista_creada.clear()
print(f"Lista eliminada: {lista_creada}")
print ("Ejercicio 7: ")
# Dada la lista mi_lista = [], usa el método reverse() para invertir el orden de los elementos y luego imprime la lista invertida.
lista_lista = [1, 2, 3, 4, 5]
print (f"Lista: {lista_lista}")
lista_lista.reverse()
print(f"Lista invertida: {lista_lista}")

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------Vamos a subir un poco el nivel -------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")

print("Ejercicio 9: ")
#Crea una lista vacía y pide al usuario que ingrese números hasta que introduzca el valor -1 (que no debe añadirse a la lista). 
# Usa el método append() para agregar los números a la lista. Luego, calcula la suma de todos los números ingresados (sin contar el -1) 
# e imprime la lista y la suma total.

lista_vacia = []
suma = 0

print ("Usuario, introduce números y cuando añadas el -1 habremos terminado: ")
while True:
    listado = int(input(f"Número: "))
    
    if listado == -1:
        print ("Programa terminado...")
        break
    else:
        lista_vacia.append(listado)
        suma = suma + listado

        
print (f"La lista queda asi: {lista_vacia}")
print(f"El sumatorio de los números de la lista es igual a: {suma}")
print("")

print ("Ejercicio 10: ")
#Tienes dos listas: mi_lista = [1, 2, 3] y otra lista vacía. 
# Pide al usuario que ingrese 3 elementos para la segunda lista, luego combina ambas listas usando extend(). 
# A continuación, elimina todos los números pares de la lista combinada y muestra la lista resultante.

lista_con_numeros = [1,2,3]
lista_sin_numeros =[]

for i in range (3):
    numeros =int(input(f"Usuario, ingresa el número {i+1}: "))
    lista_sin_numeros.append(numeros)

print(f"La lista queda asi: {lista_sin_numeros}")
lista_con_numeros.extend(lista_sin_numeros)
print(f"La lista combinada queda asi: {lista_con_numeros}")

lista_con_numeros = [x for x in mi_lista if x % 2 != 0]
print(f"Lista actualizada con numeros impares unicamente en la lista original {lista_con_numeros}")
print("")

print("Ejercicio 11: ")
#Dada la lista mi_lista = [5, 10, 15, 20], pide al usuario un número y una posición, luego inserta el número en esa posición usando insert(). 
# Si el número ya está en la lista, indica al usuario que no puede añadir duplicados. Finalmente, imprime la lista actualizada.·
lyst_n11 =[5, 10, 15, 20]
print(f"Lista original: {lyst_n11}")
numero = int(input("Usuario, dime el número que deseas introducir: "))
posicion = int (input("¿En qué posición deseas introducir el número?: "))

if numero in lyst_n11:
    print("Lo siento, no se pueden añadir duplicados... la lista se mantiene igual: ")
else:
    lyst_n11.insert(posicion, numero)

print(f"La lista actualizada con el nuevo número es: {lyst_n11}")
print("")

print("Ejercicio 12: ")
#Crea una lista de números aleatorios entre 1 y 20 con 10 elementos. 
# Luego, pide al usuario que ingrese un número y usa remove() para eliminar la primera aparición de ese número de la lista. 
# Si el número no está en la lista, informa al usuario que no se encontró y vuelve a pedir otro número hasta que se logre eliminar uno. 
# Finalmente, imprime la lista resultante.

import random

lista_random = [random.randint(1, 20) for _ in range (10)] 
print("Lista original:", lista_random)

while True:
    numero_usuario = int(input("Usuario, dime un número: ")) 

    try: 
        lista_random.remove(numero_usuario)
        break
    except ValueError:
        print("El número no esta en la lista y no se ha podido encontrar, prueba otra vez")


print("Lista actualizada:", lista_random)
print("")

print("Ejercicio 13: ")
#Dada la lista mi_lista = [100, 200, 300, 400, 500], realiza las siguientes operaciones:
#Usa pop() para eliminar el último elemento e imprime el valor eliminado y la lista.
#Usa pop() para eliminar el segundo elemento (índice 1) e imprime el valor eliminado y la lista.
#Si la lista resultante tiene más de 2 elementos, elimina otro más y muestra el valor eliminado.

lista_grande = [100, 200, 300, 400, 500]
print(f"Lista: {lista_grande}")
lista_grande.pop()
print(f"Lista actualizada: {lista_grande}")
lista_grande.pop(1)
print(f"Lista actualizada nuevamente: {lista_grande}")

if len(lista_grande) > 2:
    lista_grande.pop(1)
    print(f"Lista actualizada nuevamente para estar solo con 2 elementos: {lista_grande}")
else:
    print(f"Lista actualizada nuevamente: {lista_grande}")

print("")
print ("Ejercicio 14:  ")
#Crea una lista con al menos 10 elementos. Después, pide al usuario que confirme si quiere vaciar la lista. 
#Si elige sí, usa clear() para eliminar todos los elementos y muestra la lista vacía; si elige no, imprime la lista original sin cambios.

import random

lista_autocreada = [random.randint(1,100) for _ in range (10)]
print(f"Esta es mi lista creada automaticamente: {lista_autocreada}")
respuesta = input("¿Usuario, deseas limpiar la lista por completo? (Si/No) ")

if respuesta == "SI" or respuesta == "si":
    lista_autocreada.clear()
    print(f"Lista vacia: {lista_autocreada}")
elif respuesta == "NO" or respuesta == "no" :
    print(f"Bien usuario, mantemos nuestra lista operativa {lista_autocreada}")
else:
    print (f"La respuesta tiene que ser si o no")
    
print("")
print ("Ejercicio 15:  ")
#Crea una lista de palabras y pide al usuario que ingrese una palabra adicional. 
#Agrega la palabra a la lista y luego usa reverse() para invertir el orden de todos los elementos. 
#Imprime la lista invertida.

peliculas = ["Señor de los Anillos", "Vengadores", "Star Wars", "Harry Potter"]
print(f"Estilo de peliculas favoritas de Alberto: {peliculas}")
pelicula_adicional = input("Usuario, ingresa una pelicula que te guste: ")
peliculas.append(pelicula_adicional)
print(f"El listado de las películas actualizadas con la que dijiste usuario, queda asi: {peliculas}")
peliculas.reverse()
print(f"Alterando el orden de las peliculas, el resultado queda asi: {peliculas}")
print ("")

print("Ejercicio 16: ")
# Crea una lista que contenga tanto números como cadenas de texto. 
# Pide al usuario que ingrese un valor (puede ser un número o una palabra) y usa count() para contar cuántas veces aparece en la lista. 
# Luego, informa el resultado.

liista = [1, "hola", 2, "adiós", 1, "hola", 3]

valor = input ("Usuario, ingresa un valor: ")

if valor.isdigit():
    valor = int(valor)
    
print(f"El valor aparece en la lista un número de : {liista.count(valor)} veces")







