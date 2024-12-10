## 1) Escribe una función que reciba como argumento un string y lo imprima
print("Ejercio 1, escribir una funcion donde se reciba un string y lo imprima")

def primerFuncion(frase):
    print(frase)

primerFuncion("Esto es un string")

print(" ")

## 2) Trabajando con listas de entrada
#Escribe una función que implemente la siguiente funcionalidad
#La función recibe un solo argumento, que es una lista de números. 
#De esa lista la función imprime aquellos números que sean divisibles por 5.
print("Ejercicio 2, Creacion de funcion con números divisibles x 5")

def lista_divisible_5 (number):
    for number in lista:
        if number % 5 == 0:
            print (number)
    

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
resultado = lista_divisible_5(lista)
print(f"Los números divisibles de la lista {lista} entre 5 son: {resultado} ")
print("")

## 3) Trabajando con el retorno de una función
#Reprogramar la función anterior para que en lugar de imprimir los valores, los devuelva en forma de lista
print("Ejercicio 3, Reprogramar la función anterior para que en lugar de imprimir los valores, los devuelva en forma de lista")            
def retornar(nueva_lista):
    nueva_lista = []
    for number in lista:
        if number % 5 == 0:
            nueva_lista.append(number)
    return nueva_lista

lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
resultado_lista = retornar(lista2)
print(f"El resultado organizado en la nueva lista, es el siguiente: {resultado_lista}")
print("")

## 4) Trabajando con múltiples argumentos
##Escribe una función que implemente la siguiente funcionalidad
#La función recibe 3 argumentos que pueden ser números o strings
#La función devuelve un string con el valor de los 3 argumentos concatenados uno tras otro con el caracter "_"
#Ejemplo:
#<b>Entrada</b>:
#<ul>
#    <li>1</li>
#    <li>"a"</li>
#    <li>72</li>
#</ul>
#<b>Salida</b>:
print("Ejercicio 4, Crear una funcion que reciba 1 numero, 1 string y 1 numero, concatenarlos con _ ")

def funcion_por3 (arg1, arg2, arg3):
    return (f"{str(arg1)}_{str(arg2)}_{str(arg3)}")

numero1= 1
nombre = "Vamos a unir en este ejercicio, los números y el string"
numero2=2

union = funcion_por3(numero1,nombre,numero2)
print(f"El resultado de unir todos y cada uno de estos atributos, es el de: {union} ")
print("")

## 5) Trabajando con argumentos opcionales

"""Escribe una función que reciba 4 argumentos:

<ul>
    <li> x: Un número </li> 
    <li> y: Otro número </li> 
    <li> op: Un string cuyo valor por defecto sea "add" </li> 
    <li> ret_type: Un string cuyo valor por defecto sea "int" </li> 
</ul>

Esa función debe aplicar a "x" e "y" la operación que corresponda según el valor de "op".
<ul>
    <li> Si op == "add" los suma </li> 
    <li> Si op == "sub" los resta </li> 
    <li> Si op == "mul" los multiplica </li> 
    <li> Si op == "div" los divide </li> 
</ul>

Y luego debe de retornar en resultado de la operación anterior:
<ul>
    <li> Si ret_type == "int" lo retorna en forma de número entero redondeando el resultado </li> 
    <li> Si ret_type == "float" lo retorna en forma de float </li> 
    <li> Si ret_type == "str" retorna un string con el valor del número en él</li> 
</ul>

Llama a la función al menos de 5 maneras diferentes y en algunos de los casos deja que los valores sean los que fija por defecto en los argumentos opcionales.
"""
print("Ejercicio 5, vamos a crear una funcion con multiples opciones de trabajo, introduciendo los valores para poder operar en funcion del argumento: ")
def funcion_4_argumentos(x,y, op="add", ret_type="int"):
    if op == "add":
        resultado = x+y
    elif op == "sub":
        resultado = x-y
    elif op == "mul":
        resultado = x*y
    elif op == "div":
        if x>y:
            resultado = x/y
        else:
            return "No se puede dividir un valor tan pequeño"
    
    if ret_type=="int":
        return int(round(resultado))
    elif ret_type =="float":
        return float(resultado)
    elif ret_type == "str":
        return str(resultado)
    else:
        return "Tipo de retorno no válido"
    
    
print(funcion_4_argumentos(4,2))
print(f"El resultado de la operacion con el atributo add teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,2, "add")}")
print(f"El resultado de la operacion con el atributo sub teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,2, "sub")}")
print(f"El resultado de la operacion con el atributo mul teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,2, "mul")}")
print(f"El resultado de la operacion con el atributo div teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,2, "div")}")

print(f"El resultado de la operacion con el atributo add teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(5,7, "add", "int")}")
print(f"El resultado de la operacion con el atributo sub teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,3, "sub", "str")}")
print(f"El resultado de la operacion con el atributo mul teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(4,2, "mul", "int" )}")
print(f"El resultado de la operacion con el atributo div teniendo en cuenta que los números x = 4 e y = 2, es igual a: {funcion_4_argumentos(3,2, "div", "float")}")

print(" ")

## 6) Trabajando con número indefinido de argumentos
#Programa, una función que reciba un primer argumento llamado "op" con los valores posibles que definimos en el ejercicio anterior y luego reciba un número indeterminado de argumentos cuyo valor esperado son números
#Esta función debe de aplicar esa operación deseada al resto de argumentos en el orden indicado y devolver el resultado de dicha operación.
#Ejemplo de como tendría que funcionar esta función:
#\>\> apply_op(op="add", 1, 1, 3)"""

print("Ejercicio 6, trabajando con un número indefinido de argumentos: ")

def apply_op(op="add", *args):
    
    if len(args) == 0:
        print("Introducir un numero es el deber")
        
    resultado = args[0]

    for num in args[1:]:
        if op == "add":
            resultado += num
        elif op == "sub":
            resultado -= num
        elif op == "mul":
            resultado *=num
        elif op == "div":
            resultado /=num
    return resultado

print(f"El resultado de la operacion con el atributo add, es igual a: {apply_op("add", 4,5,2)}")
print(f"El resultado de la operacion con el atributo sub, es igual a: {apply_op("sub", 16,5,2)}")
print(f"El resultado de la operacion con el atributo mul, es igual a: {apply_op("mul", 4,5,2)}")
print(f"El resultado de la operacion con el atributo div, es igual a: {apply_op("div", 8,2)}")
print(" ")

## 7) Documentación de funciones
##Escribe una docstring para cada una de las funciones implementadas hasta el momento

print("Funcion del ejercicio 1: ")
def primerFuncion(frase):
    """
    Introduccion de una frase o palabra de caracter string

    Parametros:
    (frase) frase tipo string
    
    Retorna:
    La palabra o frase retornará la frase
    """
    print(frase)

print("Funcion ejercicio 2: ")
def lista_divisible_5 (number):
    """
    Funcion para valorar los números divisibles por 5 con un bucle for 

    Parametros:
    (number) En esta funcion se busca sacar los números divisibles por 5 dependiendo del valor de la lista

    Retornará:
    Todo número divisible por 5
    """
    for number in lista:
        if number % 5 == 0:
            print (number)
    return number

print("Función ejercicio 3: ")
def retornar(nueva_lista):
    """
    Funcion para valorar los números divisibles por 5 en una lista

    Argumentos:
    (nueva_lista) Esta función busca sacar en una lisa, nueva_lista a través de un bucle for, los números que se dividen por 5

    Retornará:
    En una lista, retornará los números divisibles por 5
    """
    nueva_lista = []
    for number in lista:
        if number % 5 == 0:
            nueva_lista.append(number)
    return nueva_lista

print("Función ejercicio 4: ")
def funcion_por3 (arg1, arg2, arg3):
    """
    Función con 3 argumentos

    Parametros
    (arg1, arg2, arg3) Introducimos 3 argumentos los cuales serán transformados a string

    Retornará
        3 strings
    """
    return (f"{str(arg1)}_{str(arg2)}_{str(arg3)}")

print("Función ejercicio 5: ")
def funcion_4_argumentos(x,y, op="add", ret_type="int"):
    """
    Funcion con varios argumentos

    Argumentos:
    (x,y, op y ret_type)   
    Nos encontramos en esta función, dos números, x e y de tipo int y dos parametros, op y ret_type de tipo string.
    En funcion del parametros, la operación entre los digitos (x, y) será diferente, por ejemplo, add = suma, sub = resta, mul = multiplicacion y div = division
    Tambien nos encontramos con tipo del valor, sea entero, float o string.
    
    Retornará:
        Retornará el resultado de la operacion entre los digitos y tambien el tipo una vez indicado, int, float o string
    """
    if op == "add":
        resultado = x+y
    elif op == "sub":
        resultado = x-y
    elif op == "mul":
        resultado = x*y
    elif op == "div":
        if x>y:
            resultado = x/y
        else:
            return "No se puede dividir un valor tan pequeño"
    
    if ret_type=="int":
        return int(round(resultado))
    elif ret_type =="float":
        return float(resultado)
    elif ret_type == "str":
        return str(resultado)
    else:
        return "Tipo de retorno no válido"
    
print ("Función ejercicio 6: ")

def apply_op(op="add", *args):
    """
    Funcion para varios argumentos
    
    Argumentos:
    (op="add", *args)
    Esta funcion tiene un atributo de tipo string inicial y varios argumentos que posteriores, teniendo en cuenta que este sea mayor de 0 digitos en todo momento.
    En función del atributo tipo string (op), nos encontraremos con que la operación a realizar será diferente en todo momento
    
    Retornará:
    La operación entre los argumentos introducidos, sea suma, resta, división o multiplicación.
    """    
    if len(args) == 0:
        print("Introducir un numero es el deber")
        
    resultado = args[0]

    for num in args[1:]:
        if op == "add":
            resultado += num
        elif op == "sub":
            resultado -= num
        elif op == "mul":
            resultado *=num
        elif op == "div":
            resultado /=num
    return resultado
print("")

## 8) Paso por referencia vs paso por valor
#Crea una función que reciba una lista de strings, y que calcule un nuevo string hecho con el comienzo de cada uno.
#Ej:
#["hello", "Susan", "hi", "sugar"] -> "hShs"
#Y que devuelva una lista con ese nuevo elemento añadido al final:
#Ej: ["hello", "Susan", "hi", "sugar", "hShs"]
#Pero que logre esto sin cambiar colateralmente ninguna variable ajena al scope de la función
print("Ejercicio 8")
def agregar_iniciales(lista_strings):
    lista_copia = lista_strings.copy()
    nuevo_string = ''.join([s[0] for s in lista_strings])
    lista_copia.append(nuevo_string)
    
    return lista_copia


lista_original = ["hello", "Susan", "hi", "sugar"]
lista_modificada = agregar_iniciales(lista_original)

print("Lista original:", lista_original)
print("Lista modificada:", lista_modificada)
print("")

## 9) Programación funcional
#Mediante la operación map y una función lambda programa un código que coja una lista de strings y genere una lista igual pero con el caracter exclamación añadido al final.
#Ej:
#["hello", "Susan", "hi", "sugar"] -> ["hello!", "Susan!", "hi!", "sugar!"]

print("Ejercicio 9:")
lista_strings = ["hello", "Susan", "hi", "sugar"]

lista_exclamacion = list(map(lambda s: s + "!", lista_strings))

print(f"Nos encontramos con esta lista y las exclamaciones : {lista_exclamacion}")
print("")

## 10) List comprehension
#Haz otro código que haga esto mismo pero usando una "list comprehension" (la sintaxis especial que en una sola línea y mediante corchetes crea una lista basada en una lista ya existente)

print("Ejercicio 10:")
lista_strings = ["hello", "Susan", "hi", "sugar"]
lista_exclamacion = [s + "!" for s in lista_strings]

print(f"Obtenemos la lista con exclamaciones y usamos list comprehension: {lista_exclamacion}")
