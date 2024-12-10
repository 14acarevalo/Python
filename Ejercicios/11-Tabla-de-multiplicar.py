##En este ejercicio vamos a realizar una tabla de multiplicar

print("Ejercicio para realizar tabla de multiplicar según el numero que introduzca el usuario: ")
nume = int(input("Usuario, ¿de qué número quieres realizar la tabla de multiplicar? "))
multiplicacion = 0

print("La tabla de multiplicar del número " +str(nume)+ " teniendo en cuenta los dígitos del 1 al 10, es: ")
for num in range (1, 11):
    multiplicacion = nume *num
    print (str(nume)+ " x " +str(num)+ " es igual a: " +str(multiplicacion))
print("")
print(" ")   
    
##A continuación, se añade otro ejercicio con el objetivo de meter varias tablas de multiplicar

print("Tablas de multiplicar: ")
print(" ")

for num1 in range (1, 11):
    print("Tabla de multiplicar del número " +str(num1))
    for num2 in range (1, 11): ## Cuando termine el bucle completo del 1 al 10, se suma un numero en num1, es decir, del 1 al 2... y se repite la tabla de multiplicar
        print(str(num2)+ " x " +str(num1)+ " = "  +str(num2*num1) )
    print(" ")
        