# Completa las celdas vacías implementando la funcionalidad pedida
## 1) Escrible un código que imprima "Hola Mundo"
print("Ejercicio 1: ")
print("Hola Mundo!!")
print(" ")
## Otra forma de hacerlo
saludo = "Hola Mundo!"
print(saludo)
print(" ") ##Espaciador entre ejercicios

## 2) Creación y uso de variables simples
## Crea una variable numérica con valor 10
## Crea una variable de tipo cadena de caracteres con valor "abcd"
## Imprime el valor y el tipo de cada una de ellas
##Imprime un string que sea resultado de unir ambas variables con una "_" de por medio, no olvides realizar los casting que sean necesarios para que la concatenación pueda funcionar, la salida tendría que quedar estilo "10_abcd"
## Luego elimina ambas variables

print("Ejercicio 2: ")
variable_int = 10
variable_string = "abcd"
print("Variable 1: " +str(variable_int))
print("Variable 2: " +variable_string)
print("La variable cuyo valor es igual a = 10, es una variable de tipo: " )
print(type(variable_int))
print("La variable cuyo valor es igual a = abcd, es una variable de tipo: " )
print(type(variable_string))
print("Concatenación: ")
concatenacion = str(variable_int) + "_" +variable_string
print("La union de ambas variables, es decir, la concatenacion es igual a : " +str(concatenacion))
print("Delete")
del variable_int
del variable_string

print(" ") ##Espaciador entre ejercicios

## 3) Trabajando con números
##Crea dos variables, una llamanda num_1 con valor 5 y otra llamada num_2 con valor 10.5
##Calcula lo siguiente: ((num_1 - num_2)**num_1)*12.5
##Almacena el resultado de la operación anterior en una variable llamada num_res
##Calcula el resultado de dividir el valor absoluto de num_res entre 12.22 y actualiza el valor de num_res con este nuevo resultado
##Redondea el número num_res a 2 cifras decimales
##Crea una nueva variable llamada num_res_int que contenga el suelo entero de valor actual de num_res

print("Ejercicio 3: ")
num_1 = 5
num_2 = 10.5
print("Las variables creadas son: " +str(num_1)+ " y " +str(num_2))
num_res = ((num_1-num_2)**num_1)*12.5
print("Realizamos la operacion matematica pedida en el enunciado: " +str(num_res))
division = num_res /12.22
print("Realizamos una operacion de división: " +str(division))
redondeo = round(division,2) ##Nota: Round me sirve para redondear el valor de la variable division a 2 decimales
redondeo1 = round(division,1) ##Nota: Esta es otro ejemplo, sólo por ver el valor reflejado y aprender
print("Esta es de prueba para practicar y aprender más " +str(redondeo1))
print("Redondeo pedido por el enunciado: " +str(redondeo)) ## Pongo este comando para asegurarme de que el valor de redondeo se muestre por pantalla y sea igual a num_res_int
num_res_int = redondeo
print("Nueva variable con un valor entero: " +str(num_res_int))
print(" ") ##Espaciador entre ejercicios

## 4) Trabajando con strings
##Crea una variable llamada string_1 que contenga el texto:
##<i>"La astrofísica es el desarrollo y estudio de la física aplicada a la astronomía.<br>
##Estudia las estrellas, los planetas, las galaxias, los agujeros negros y demás objetos astronómicos como cuerpos de la física, incluyendo su composición, estructura y evolución. <br>
##La astrofísica emplea la física para explicar las propiedades y fenómenos de los cuerpos estelares a través de sus leyes, fórmulas y magnitudes."</I>
##Recuerda introducir el caracter especial correspondiente para que se respeten los saltos de línea especificados
##Luego haz lo siguiente:
##<li> Imprime el texto completo
##<li> Imprime la longitud del texto
##<li> Imprime los caracteres con índices del 1 al 6
##<li> Imprime los caracteres desde el 6 al final
##<li> Imprime si la secuencia de caracteres "WAF" se encuentra o no en el texto (True o False)
##<li> Imprime una versión del string con todos sus caracteres en minúscula

print("Ejercicio 4: ")
texto = "La astrofísica es el desarrollo y estudio de la física aplicada a la astronomía. \nEstudia las estrellas, los planetas, las galaxias, los agujeros negros y demás objetos astronómicos como cuerpos de la física, incluyendo su composición, estructura y evolución. \nLa astrofísica emplea la física para explicar las propiedades y fenómenos de los cuerpos estelares a través de sus leyes, fórmulas y magnitudes."
print(texto) 
print("La longitud del texto es: " +str(len(texto))) ##Para contar la magnitud del texto 
texto_reducido = texto[1:6]
print("Reducción del texto: " +texto_reducido)
text_ampliado = texto[6:405]
print("Ampliación del texto: " +text_ampliado)
buscar = texto.count("WAF")
print("Vamos a buscar una palabra conocido como WAF " +str(buscar))
minusculas = texto.lower() ##Comando para reducir
print("Texto en minúsculas: " +minusculas)
## reducir = [palabra.lower() for palabra in texto] ##prueba de otro comando
## print(reducir)
print("El texto de nuevo es: " +texto)
print(" ")

## 5) Trabajando con Booleanos
##Crea dos variables, una llamda var_1 con valor True y otra llamada var_2 con valor False
##¿Cuál es el resultado de hacer un "and" ente ambas?
##¿Cuál es el resultado de hacer un "or" ente ambas?
##¿Cuál es el resultado de hacer un "not" de var_2?

print("Ejercicio 5: ")
var_1 = True
var_2 = False
print(var_1 and var_2) ##False
print(var_1 or var_2) ##True
print(not var_2) ##Lo contrario, es decir, TRUE

#### 6) Trabajando con listas
##Crea estas dos listas:
##<li>list_1 = ["a", "b", "c"]
##<li>list_2 = [1, 2, 3, 4]
##<br><br>
##Imprime el primer elemento de la lista list_1
##Imprime el tercer elemento comenzando por la derecha de list_2
##Imprime el número que tenga el valor máximo en list_2
##Crea una lista llamada list_cat que sea la concatenación de las dos listas  
##Añade a list_cat un nuevo elemento con valor 12.5  
##Imprime la longitud de list_cat   
##Remplaza el elemento número 3 de list_cat por el valor "x" 
##Elimina el item con índice 2 de list_cat 
##Crea una nueva variable que se llame list_1_sorted con la lista 1 ordenada

print("Ejercicio 6a: ")
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3, 4]
primer_elemento = list_1 [0]
print("Primer elemento de la lista 1: " +str(primer_elemento))
tercer_elemento = list_2 [-3]
print("Tercer elemento de la lista 2: " +str(tercer_elemento))
maximo = max(list_2)
print("Número con más valor correspondiente a la lista 2: " +str(maximo))
list_cat = list_1 + list_2
print("Concatenacion de listas: " +str(list_cat))
list_cat.append(12.5)
print("Añadimos un valor de 12.5: " +str(list_cat))
print("Vamos a imprimir la longitud de la lista: " +str(len(list_cat)))
list_cat.insert(6, "x")
print("Reemplazamos un valor por la letra x: " +str(list_cat))
list_cat.pop(2)
print("Ponemos la lista actualizada, tras eliminar el item con indice 2: " +str(list_cat))
list_1_sorted = list_1.sort()
print("Procedemos a crear una nueva variable, conocida como list_1_sorted: ")
print(list_1_sorted)
print(" ")

## 6) Trabajando con tuplas
##Intenta hacer todos los pasos anteriores pero usando tuplas, algunos de ellos fallarán, explica brevemente por qué ocurre esto y cuál es la utilidad de este comportamiento.

print("Ejercicio 6b: ")
my_tupla1 = ("a", "b", "c")
my_tupla2 = (1, 2, 3)

print("Primer elemento de la tupla 1: ")
primer_elemento_tupla = my_tupla1[0]
print(primer_elemento_tupla)

print("Tercer elemento de la tupla 2: ")
tercer_elemento_tupla = my_tupla2[-3]
print(tercer_elemento_tupla)

print("Valor máximo de la tupla 2: ")
print(max(my_tupla2))

fusión_tuplas = my_tupla1 + my_tupla2
print("La unión de las tuplas: " + str(fusión_tuplas))

# No podemos hacer append ni otros métodos de modificación porque las tuplas son inmutables
# Este comportamiento es útil cuando queremos asegurar que nuestros datos no se modifiquen accidentalmente
print("No podemos modificar las tuplas, ya que son inmutables.")
print(" ")


## 7) Trabajando con diccionarios
##Crea un diccionario vacío y rellénalo con estos datos (entendiéndose como pares clave-valor):
##<li> "58195348N": "Pepito Pérez"
##<li> "96173220P": "Juanito Martínez"
##<li> "43740289Q": "Adolfo Rodríguez"
##<li> "41588605M": "Roberto García"
##Consulta el diccionario, ¿Cuál es el nombre de la persona con DNI "96173220P"?
##Cambia el nombre asociado a la clave "41588605M" por "Roberto Martínez"  
##Elimina la entrada correspondiente a la clave "96173220P" 
##Imprime la longitud del diccionario  
##Imprime si la clave "99114051J" está o no en el diccionario (True o False)

print("Ejercicio 7: ") 
diccionario = {
    "58195348N": "Pepito Pérez",
    "96173220P": "Juanito Martínez",
    "43740289Q": "Adolfo Rodríguez",
    "41588605M": "Roberto García"
}

print("El nombre de la persona con DNI '96173220P' es: " + diccionario["96173220P"])

diccionario["41588605M"] = "Roberto Martínez"
print("Se ha actualizado el nombre asociado a '41588605M': " + diccionario["41588605M"])

del diccionario["96173220P"]
print("Se ha eliminado la entrada con DNI '96173220P'.")

print("La longitud del diccionario es: " + str(len(diccionario)))

existe_clave = "99114051J" in diccionario
print("¿La clave '99114051J' está en el diccionario? " + str(existe_clave))
print(" ")


## 8) Trabajando con conjuntos
##Crea una lista con los siguientes valores
##<li>[1,2,2,2,3,2,3,5,1]
##Convierte esta lista a otra lista que no contenga elementos repetidos
##Crea los dos siguientes conjuntos:
##<li>conj_1 = {1,2,3,4,5}
##<li>conj_2 = {3,4,5,6,7}  
##Comprueba si el elemento 10 está en el conjunto 1
##¿Son conjuntos disjuntos?
##¿Es conj_1 un subconjunto de conj_2?   
##Calcula los elementos que estén en conj_1 pero no en conj_2  
##Calcula los elementos comunes a ambos conjuntos

print("Ejercicio 8: ") 
lista_valores = [1, 2, 2, 2, 3, 2, 3, 5, 1] ##Creo mi lista

# Convertir lista a conjunto para eliminar duplicados utilizando el set
lista_sin_duplicados = list(set(lista_valores))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

##Creo los conjuntos 1 y 2
conj_1 = {1, 2, 3, 4, 5}
conj_2 = {3, 4, 5, 6, 7}

# Compruebo si el elemento 10 está en conj_1 con in
print(f"¿Está el 10 en conj_1? {10 in conj_1}")

# Verifico si los conjuntos son disjuntos con isdisjoint
print(f"¿Son disjuntos? {conj_1.isdisjoint(conj_2)}")

# Verifico si conj_1 es subconjunto de conj_2 con issubset
print(f"¿Es conj_1 subconjunto de conj_2? {conj_1.issubset(conj_2)}")

# Calculo elementos en conj_1 pero no en conj_2 con la resta
print(f"Elementos en conj_1 pero no en conj_2: {conj_1 - conj_2}")

# Calculo elementos comunes en ambos conjuntos
print(f"Elementos comunes a ambos conjuntos: {conj_1 & conj_2}")




## 9) Trabajando con if, if-else, if-elif
##Tenemos dos variables, les asignamos inicialmente estos valores:
##<li>var_1 = [0, 1]
##<li>var_2 = [0,1,2,3,4,5]
##Implementar la siguiente lógica:
##<li>Si la longitud de var_1 es mayor que la de var_2 imprimimos "var_1 tiene longitud mayor que var_2"
##<li>Si la condición anterior no se cumple y la longitud de var_1 es igual que la de var_2 imprimimos "var_1 tiene longitud igual que var_2"
##<li> Si la condición anterior no se cumple y si el elemento en el índice 0 de var_1 es igual al elemento del índice 0 de var_2 imprimimos "Ambas listas comienzan por el mismo valor"
##<li>Si no se cumple nada de lo anterior imprimimos "No se cumple ninguna de las condiciones"
##<br><br>
##<li> Si el elemento en el índice 0 de var_1 es igual al elemento del índice 0 de var_2 y el elemento en el índice 1 de var_1 es igual al elemento del índice 1 de var_2 imprimimos "Ambas listas comienzan por los dos mismos valores"
##<li> Si la condición anterior no se cumple, imprimimos: "Al menos uno de los dos primero valores de ambas listas son diferentes"
##<br><br>

print("Ejercicio 9: ") 
var_1 = [0,1]
var_2 = [0,1,2,3,4,5]

if len(var_1) > len(var_2):
    print("Var_1 tiene una longitud mayor que la de var_2")
elif  len(var_1) == len(var_2):
    print("Las variables son iguales")
elif var_1[0] == var_2[0] :
    print("Ambas listas empiezan por el mismo valor")
    if var_1[0] == var_2[0] and var_1[1] == var_2[1] :
        print("Ambas listas comienzan por los dos mismos valores")
    else:
        print("Al amenos uno de los dos primeros valores de ambas listas son diferentes")
else:
    print("No se cumple ninguna condicion")
##if var_1[0] == var_2[0] and var_1[1] == var_2[1] :
   ## print("Ambas listas comienzan por los dos mismos valores")
##else:
    ##print("Al amenos uno de los dos primeros valores de ambas listas son diferentes")

##Ambos codigos funcionan, pero siguiendo la lógica aplastante, se pone esta última condición dentro de elif var_1[0] == var_2[0] :
## ya que estamos comparando el primer número y el segundo de cada variable

print (" ")
## 10) Trabajando con for y while
##Tenemos las siguientes listas:
##<li>char_list = ["a", "b", "c", "d"]
##<li>num_list = [1, 2, 3, 4]
##Realizar un bucle for que recorra num_list e imprima sus valores y además el caracter que se encuentra en la misma posición en char_list

print("Ejercicio 10: ") 
char_list = ["a", "b", "c", "d"]
num_list = [1, 2, 3, 4]

##Opcion 1
for numero in num_list:
    print(str(numero))

##Opcion 2
for i in range(len(num_list)):
    print(f"num_list[{i}]: {num_list[i]}, char_list[{i}]: {char_list[i]}")

print("Realizamos el ejercicio 10 con while: ")    
i = 0
# El bucle while recorrera todo mientras este dentro del indice
while i < len(num_list):
    print(f"num_list[{i}]: {num_list[i]}, char_list[{i}]: {char_list[i]}")
    i += 1