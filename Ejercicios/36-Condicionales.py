## En este reto, nos vamos a encontrar con diferentes ejercicios de condicionales, con el fin de prácticar y trabajar lo desarrollado.

##Ejercicio 1 - Escribir un programa que nos pida la edad y si somos o no mayores de edad.

print("Usuario, en este programa vamos a necesitar tu edad: ")
edad = int(input("Usuario, dime tu edad: "))

if edad > 18:
    print (f"Usuario, tienes {edad} años y eres mayor de edad!!!!!!!")
elif edad < 18 and edad >= 1:
    print (f"No has cumplido la mayoria de edad")
else:
    print("Introduce un dato valido, porque según esto no has nacido todavia!!!! ")

print("")

##Ejercicio 2 - Escribir un programa donde se nos pida la contraseña, se almacene en una variable y si introducimos y es la correcta, premio!!

contraseña = "contraseña"

print("Usuario, introduce la contraseña ")
password = input("")

if password == contraseña:
    print("Contraseña correcta!!!!!!!")
else:
    print("ERROR!!") 
print(" ")   
##Ejercicio 3 - Escribir un programa donde se pidan dos números al usuario y se muestre la división por pantalla. Si el divisor es 0 es un error

dividendo = int(input("Usuario, dame el dividendo de tu operación matemática: "))
divisor = int(input("Usuario, dame el divisor de tu operación matematica: "))
division = dividendo/divisor

if dividendo > 0 and dividendo >= divisor:
    print(f"El resultado de tu operacion es igual a: {division}")
else:
    print("No se puede efectuar dicha división...")
print(" ")   

##Ejercicio 4 - Numero par y/o impar
print("Usuario, dame un número: ")
number = int(input())
if number % 2 == 0:
    print(f"El número {number} es par")
else:
    print(f"El número {number} es impar")
print("")

##Ejercicio 5 - Tributa - Programa donde el usuario muestre si tiene más de 16 años y unos ingresos iguales y/o superiores a 1000 € mensuales, si es asi, puede tributar
print("Usuario, vamos averiguar si puedes tributar o no")
edad = int(input("Usuario, dame tu edad: "))
ingresos = (int(input("Usuario, pon tus ingresos: ")))

if edad >= 16 and ingresos >= 1000:
    print(f"Usuario, puedes tributar ya que tu edad es igual a {edad} y tienes unos ingresos de {ingresos} €")
if edad >= 16 and ingresos < 1000:
    print("Usuario, vuelve cuando tengas unos ingresos superiores o igual a 1000 €")
if edad < 16 and ingresos > 1000:
    print("Usuario, todavia no tienes la edad mínima estipulada")

print("")
##Con un simple if y un else se podria hacer, pero en este caso he querido especificar un poco más

##Ejercicio 6 - Ordenar las clases - Divide los grupos en A y B según el sexo y el nombre. El grupo A esta formado por mujeres con un nombre anterior a M y los hombres con un nombre posterior a la N. EL B el resto
print("En este programa, se busca establecer a que grupo va a ir cada alumno")
name = input("Usuario, introduce tu nombre: ").capitalize()
sexo = input("Usuario, introduce tu sexo (hombre o mujer): ").upper()

if (sexo == "M" and name [0] < "M") or (sexo == "H" and name [0] > "N"):
    print ("Perteneces al grupo A")
else:
    print ("Perteneces al grupo B ")

print("")

##Ejercicio 7 - Renta - Realizar un porcentaje de declaración de la renta según el requisitio de ingreso:

print("En este programa vamos a calcular tu renta, según tus ingresos")
print("Usuario, introduce tu renta: ")
renta = int(input())

if renta < 10000:
    print(f"Tu tipo impositivo es de un 5%, por lo tanto, tu renta es igual a {renta - (renta*5)/100}")
elif renta <= 10000 and renta < 20000 :
    print(f"Tu tipo impositivo es de un 15%, por lo tanto, tu renta es igual a {renta - (renta*15)/100}")
elif renta <= 20000 and renta < 35000 :
    print(f"Tu tipo impositivo es de un 20%, por lo tanto, tu renta es igual a {renta - (renta*20)/100}")
elif renta <= 35000 and renta < 60000 :
    print(f"Tu tipo impositivo es de un 30%, por lo tanto, tu renta es igual a {renta - (renta*30)/100}")
elif renta < 60000 :
    print(f"Tu tipo impositivo es de un 45%, por lo tanto, tu renta es igual a {renta - (renta*45)/100}")

##Ejercicio 8 - Evaluar al trabajador según su nivel

salario = 2400
nivel = input("Jefe, ¿cómo evaluas este año a tu trabajador? (inaceptable, aceptable, meritorio) ")

if nivel == "inaceptable":
    print (f"Salario es igual a: {salario}")
elif nivel == "aceptable":
    print (f"Salario es igual a: {(salario*0.4)+salario}")
elif nivel == "meritorio":
    print (f"Salario es igual a: {(salario*0.6)+salario}")

##Ejercicio 9 - Sala de juegos y precio a los clientes

print("En este programa, vamos a saber si el usuario puede entrar a la sala, dependerá de su edad")
edad=int(input("Por favor, introduce la edad: ")) 

if edad < 4:
    print("Entrada gratis ")
elif edad > 4 and edad < 18:
    print("Tienes que pagar 5 €")
elif edad > 18:
    print("Tienes que pagar 10 €")
    
    
##Ejercicio 10 - Restaurante - elección de pizza y en funcion de esta, se muestra los ingredientes: 

print("Bienvenido a la pizzeria Bella Napoli, te ofreremos varias pizzas, vegetarianas y no vegetarianas ")
print("Por favor, escoge una opcion: (vegetariana / no vegetariana)")
pizza = input(" ")

if pizza == "vegetariana":
    print("Los ingredientes son: Pimiento y tofu")
else:
    print("Los ingredientes son: Peperoni, jamón y salmón")    