## Ejercicio 1: Crear y Acceder a Tuplas
##Crea una tupla llamada info_personal que contenga los siguientes elementos: tu nombre, tu edad, tu altura (en metros), y tu ciudad de residencia.
##Imprime cada uno de los elementos de la tupla accediendo a ellos por su índice.
##Imprime el último elemento de la tupla usando un índice negativo.

info_personal = ("Alberto" , 30, 1.85, "Toledo") ##Creo mi tupla
print(f"Mi nombre es: {info_personal[0]}")
print(f"Mi edad es: {info_personal[1]}")
print(f"Mi estatura en metros es: {info_personal[2]}")
print(f"Mi residencia es: {info_personal[3]}")

print(" ")
print(f"El total de mis datos son: {info_personal}")
print(f"Siguiendo un indice negativo, el último dato es: {info_personal[-1]}")
print("")
##Ejercicio 2: Operaciones Básicas con Tuplas
##Crea una tupla llamada numeros que contenga los números del 1 al 5.
##Cuenta cuántas veces aparece el número 3 en la tupla numeros.
##Encuentra el índice del número 4 en la tupla numeros.

numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)  ##Creo mi tupla
print(f"La tupla con todos los números es la siguiente: {numeros}")
print(f"El número de veces que aparece el número 3 en esta tupla es de: {numeros.count(3)}")
print(f"El indice del número 4 en esta tupla es el de: {numeros.index(4)}")
print("")
##Ejercicio 3: Slicing y Concatenación de Tuplas
##Crea dos tuplas:
##primera_parte que contenga los primeros tres días de la semana.
##segunda_parte que contenga los últimos cuatro días de la semana.
##Concatena ambas tuplas en una nueva tupla llamada semana_completa.
##Haz un slicing de semana_completa para obtener una nueva tupla que contenga solo los días laborales (de lunes a viernes).

primera_parte = ("Lunes" , "Martes" , "Miercoles")
segunda_parte = ("Jueves", "Viernes", "Sábado", "Domingo")
print(f"Los primeros 3 días de la semana son: {primera_parte}" )
print(f"Los últimos 4 días de la semana son: {segunda_parte}" )
concatenacion_tuplas = primera_parte +segunda_parte
print(f"Los días de la semana fusionando ambas tuplas son:  {concatenacion_tuplas}")
print(f"Vamos con el Slicing, en donde podemos encontrarnos con: {concatenacion_tuplas[0:5]}")
print(" ")

##Ejercicio 4: Modificación de Tuplas mediante Listas
##Convierte la tupla semana_completa en una lista.
##Reemplaza el segundo día de la semana (martes) por "Martes Modificado".
##Añade un nuevo día llamado "Funday" al final de la lista.
##Convierte la lista modificada de nuevo en una tupla llamada semana_modificada.
##Imprime la tupla semana_modificada.
semana_completa = ("Lunes" , "Martes" , "Miercoles","Jueves", "Viernes", "Sábado", "Domingo")
print(type(semana_completa))
print("Como se puede observar anteriormente, aqui tenemos la misma información pero en tupla")
##Como se puede observar, una tupla no se puede modificar, pero si la cambiamos a lista, la cosa cambia
semana_completa_lista = list(semana_completa)
print(type(semana_completa_lista))
print("Como se puede observar anteriormente, aqui tenemos la misma información pero en lista")
semana_completa_lista[1] = "Martes Modificado"
print(semana_completa_lista)
semana_completa_lista.insert(8, "Funday")
print(semana_completa_lista)
semana_completa_tupla = tuple(semana_completa_lista)
print(semana_completa_tupla)
print(type(semana_completa_tupla))

##Ejercicio 5: Manipulación de Tuplas y Slicing
##Crea una tupla llamada datos que contenga los siguientes elementos:

#Un nombre (cadena de texto)
#Una edad (entero)
#Una altura (flotante)
#Una lista de hobbies (lista de cadenas de texto)
#Usa slicing para obtener una nueva tupla que contenga solo los primeros dos elementos de la tupla original.

#Desempaqueta la tupla datos en variables separadas y luego construye una nueva tupla con el nombre y la altura invertidos.

#Crea una nueva tupla llamada datos_modificados que contenga los mismos elementos que la tupla original datos, pero reemplaza la lista de hobbies con una nueva lista que contenga dos hobbies adicionales.

datos = ("Alberto", 30, 1.85, "Cine", "Deporte", "Comida")
print(f"Hemos creado nuestra tupla, donde los datos son los siguientes: {datos}")
print(f"Procedemos a un slicing en donde los dos primeros datos son: {datos[0:2]}")
datos_modificados = datos
print(f"La creacion de la nueva lista es: {datos_modificados}")
datos_modify = list(datos_modificados)
print(f"Hemos pasado nuestra tupla a lista y lo comprobamos: {type(datos_modify)}")
datos_modify[3] = "pasear"
datos_modify[4] = "dormir"
datos_modify[5] = "conducir"
print(f"La nueva lista actualiza es: {datos_modify}")
datos_modify1=tuple(datos_modify)
print(f"Hemos transformado la lista a tupla, y obtenemos esto: {datos_modify1} y {type(datos_modify1)}")
print(" ")

#Ejercicio 6: Operaciones Avanzadas con Tuplas
#Crea una tupla llamada nombres que contenga cinco nombres de personas.

#Usa la función sorted para obtener una nueva tupla nombres_ordenados que contenga los nombres en orden alfabético.

#Cuenta cuántas veces aparece el nombre "Ana" en la tupla nombres.

#Encuentra el índice del primer nombre que empiece con la letra "J" y reemplázalo con el nombre "Javier".

nombres_personas = ("Alberto", "Pablo", "Fernando", "Isabel", "Sandra")
print(f"Creamos tupla: {nombres_personas}")
nombres = tuple(sorted(nombres_personas))
print(f"Vamos a ordenar los nombres: {nombres} ")
print(f"El nombre de Ana aparece un total de: {nombres_personas.count("Ana")} veces" )

#Ejercicio 7: Funciones con Tuplas
#Crea una función llamada fusionar_tuplas que tome dos tuplas como parámetros y devuelva una nueva tupla que sea la concatenación de las dos tuplas.

#Crea otra función llamada filtrar_tupla que tome una tupla y un valor como parámetros y devuelva una nueva tupla que contenga solo los elementos de la tupla original que sean distintos al valor dado.

#Prueba ambas funciones con ejemplos de tuplas y valores para verificar su funcionamiento.

tupla1 = (1,2,3,4)
print(f"Imprimimos la tupla 1: {tupla1}")
tupla2 = (5,6,7,8)
print(f"Imprimimos la tupla 2: {tupla2}")

fusionar_tuplas = tupla1 + tupla2

print(f"La fusión de las tuplas es la siguiente: {fusionar_tuplas}")
filtrar_tupla = fusionar_tuplas [0:3]
print(f"La tupla 1 es: {filtrar_tupla}")

#Ejercicio 8: Conversión y modificación
#Crear una tupla llamada productos con nombre, precio y cantidad
#Pasamos esta tupla a lista y se añade el codigo del producto
#Volvemos a convertirla en tupla
#Crea una funcion

productos = ("Tomate", 2.14, 2)
productos_actualizados = list(productos)
productos_actualizados.insert(3, 1632)
print(f"Mi lista de productos actualizados, en donde nos encontramos que es de tipo {type(productos_actualizados)} contiene: {productos_actualizados}")
productos_modificados = tuple(productos_actualizados)
print(f"Volvemos a transformar nuestra lista en una tupla, en donde podemos ver como es de tipo {type(productos_modificados)} y en ella están {productos_modificados}")

def calcular_valor_inventario(productos):
    nombre, precio, cantidad, codigo = productos
    return precio*cantidad

valor_final_tupla = calcular_valor_inventario(productos_modificados)
print(f"El precio final teniendo en cuenta la cantidad solicitada es de: {valor_final_tupla} teniendo en cuenta que nos encontramos con una lista {type(productos_modificados)}")


valor_final_lista = calcular_valor_inventario(productos_actualizados)
print(f"El precio final teniendo en cuenta la cantidad solicitada es de: {valor_final_lista} teniendo en cuenta que nos encontramos con una lista {type(productos_actualizados)}")

#Ejercicio 9: Análisis de venta con tuplas
##Se debe de buscar el total de ventas, el dia de mayor venta, promedio y filtrar ventas

ventas_diarias = (
    ("Lunes" , 305.5),
    ("Martes" , 489),
    ("Miercoles" , 123.2),
    ("Jueves" , 400.8),
    ("Viernes", 543.3),
    ("Sábado", 600.7),
    ("Domingo", 250.1)
)

def total_ventas (ventas_diarias):
    return sum(venta for dia, venta in ventas_diarias)

cantidad_total = total_ventas(ventas_diarias)
print(f"El total de la cantidad que nos podemos encontrar es de: {cantidad_total}")

def promedio_ventas(ventas_diarias):
    return sum(venta for dia, venta in ventas_diarias)/len(ventas_diarias)

media_ventas = promedio_ventas(ventas_diarias)
print(f"La media total de ventas es igual a: {media_ventas}")

