##Vamos a crear un programa con funcion que tenga en cuenta si el número que introducimos es par, primo y calcule el fibonacci


def operacion_matematica(num1):
    if num1 >0:
        print("Numero introducido mayor que 0, es fibonacci")
        if num1 % 2 !=0 or num1 == 2 :
            print("El numero " +str(num1)+ " es primo ")
        else:
            print("El numero " +str(num1)+ " NO es primo ")

    else:
        print("Por favor, el número tiene que ser mayor que 0")
    if num1 % 2==0: 
        print("El numero " +str(num1)+ " es par ")
    else:
        print("El numero " +str(num1)+ " es impar ")
    
    return num1


numero = int(input("Usuario, introduce un número entero: "))
resultado = operacion_matematica(numero)

    

        
    
        