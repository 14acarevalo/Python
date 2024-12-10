##Ejercicio 1: Par o impar

mi_numero = int(input("Usuario, introduce un número: "))

if mi_numero % 2 == 0:
    print("El número " +str(mi_numero)+ " es par")
else :
    print("El número " +str(mi_numero)+ " es impar")

print(" ")

##Ejercicio 2: Edad y etapa de la vida. Pedimos edad y según la edad, nos encontrams en una etapa de la vida

edad = int(input("Usuario introduce tu edad: "))

if edad <= 18:
    print("Eres menor de edad ")
elif edad > 18 and edad <26 :
    print("Eres un adolescente")
elif edad >26 and edad <65 :
    print("Eres un adulto ")
elif edad > 65:
    print("Estas jubilado ")
else:
    print ("Por favor, introduce bien tu edad")
    
print (" ")

##Ejercicio 3. Calificaciones de examen

nota = float(input("Usuario ¿qué nota has optenido en el examen? "))

if nota <5:
    print("Estás suspenso ")
elif nota >= 5  and nota <= 6 :
    print("Tu calificacion es de bien")
elif nota > 6 and nota <= 8 :
    print("Tu calificacion es de notable")
elif nota > 8 and nota <=8.9:
    print("Tu calificacion es de notable alto ")
else:
    print ("Has sacado un sobresaliente")
    
print (" ")

##Ejercicio 4 de calculadora
print("Vamos a realizar una operación matemática usuario de suma ")
operando1 = float(input("Usuario, introduce el primer número: "))
operando2 = float(input("Usuario, introduce el segundo numero: "))

suma = operando1 + operando2

if suma > 0 :
    print ("Hemos conseguido un valor por encima de 0 ")
else :
    print("El resultado de tu operacion es igual a un número menor que 0")
print(" ")

##Ejercicio 5 de operaciones

print("Vamos a realizar una operación matemática usuario ")
operando3 = float(input("Usuario, introduce el primer número: "))
operando4 = float(input("Usuario, introduce el segundo numero: "))
simbolo = input("Usuario introduce un simbolo (+ , - , / , *) ")

if simbolo == "+":
    suma = operando3 + operando4
    print("Vamos a realizar una suma, donde obtendremos " +str(suma)+ " como resultado")
elif simbolo == "-":
    resta = operando3 - operando4
    print("Vamos a realizar una resta, donde obtendremos " +str(resta)+ " como resultado")
elif simbolo == "*":
    multiplicacion = operando3*operando4
    print("Vamos a realizar una multiplicacion, donde obtendremos " +str(multiplicacion)+ " como resultado")
elif simbolo == "/":
    division=operando3/operando4
    if operando3>operando4:
        print("Vamos a realizar una divison, donde obtendremos " +str(division)+ " como resultado")
    else :
        print("No se puede realizar la operación ya que el primer número es más pequeño que el segundo")
else :
    print("El simbolo no se corresponde con ninguna operacion")
print(" ")

##Ejercicio 6 de operaciones

print ("Calculadora de IMC: ")
altura = float(input("Usuario, introduce tu altura en metros: "))
peso = float(input("Usuario, introduce tu peso en kg "))
imc = peso/(altura**2)

if imc <18.5 :
    print("Estás por debajo del peso recomendado, ya que tu IMC es igual a " +str(imc))
elif imc >= 18.5 and imc<24.9:
    print("Estás en una categoria normal, ya que tu IMC es igual a " +str(imc))
elif imc >= 24.9 and imc<29.9:
    print("Sobrepasas un poquito el imc correspondiente a un peso normal, ya que tu IMC es igual a " +str(imc))
elif imc >= 30 and imc< 32:
    print("")
else :
    print("Chicooooooooo, cuidate que estás rozando unos indices muy peligrosos")

print("")

##Ejercicio 7: ¿Qué número es el mayor?
print("Usuario, necesito que introduzcas 3 numeros y vamos a comprobar cual es el mayor")
numero_1 = int(input("Usuario, introduce el número 1: "))
numero_2 = int(input("Usuario, introduce el número 2: "))
numero_3 = int(input("Usuario, introduce el número 3: "))

if numero_1 > numero_2 and numero_1 > numero_3 :
    print("El número 1, " +str(numero_1)+ " es el mayor de los numeros")
elif numero_2 > numero_1 and numero_2 > numero_3 :
    print("El número 2, " +str(numero_2)+ " es el mayor de los numeros")
elif numero_2 == numero_1 or numero_2 == numero_3 or numero_1 == numero_3 :
    print("Nos encontramos ante dos números del mismo tamaño, por lo tanto los dos números son igual de grandes ")
else :
    print("El número 3, " +str(numero_3)+ " es el mayor")
print(" ")

##Ejercicio 7: Calculadora Avanzada
print("Vamos a realizar una operación matemática usuario ")
operando3 = float(input("Usuario, introduce el primer número: "))
operando4 = float(input("Usuario, introduce el segundo numero: "))
simbolo = input("Usuario introduce un simbolo (+ , - , / , * , ** , %) ")

if simbolo == "+":
    suma = operando3 + operando4
    print("Vamos a realizar una suma, donde obtendremos " +str(suma)+ " como resultado")
elif simbolo == "-":
    resta = operando3 - operando4
    print("Vamos a realizar una resta, donde obtendremos " +str(resta)+ " como resultado")
elif simbolo == "*":
    multiplicacion = operando3*operando4
    print("Vamos a realizar una multiplicacion, donde obtendremos " +str(multiplicacion)+ " como resultado")
elif simbolo == "/":
    division=operando3/operando4
    if operando3>operando4:
        print("Vamos a realizar una divison, donde obtendremos " +str(division)+ " como resultado")
    else :
        print("No se puede realizar la operación ya que el primer número es más pequeño que el segundo")
elif simbolo == "**":
    cuadrado = operando3**operando4
    print("Vamos a realizar una operacion de elevación, donde obtendremos " +str(cuadrado)+ " como resultado")
elif simbolo == "%":
    modulo = operando3%operando4
    print("Vamos a realizar una multiplicacion, donde obtendremos " +str(modulo)+ " como resultado")
else :
    print("El simbolo no se corresponde con ninguna operacion")
print(" ")

##Ejercicio 8: Año bisiesto
print("Usuario, introduce un año y sabremos si es o no bisiesto ")
anio = int(input("¿Qué año vas a introducir? : "))

if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0) :
    print("El año es bisiesto")
else :
    print("El año no es bisiesto")    

    