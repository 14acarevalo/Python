##En este programa vamos a crear una funcion que sume 2 números enteros y retorne su resultado pasado unos segundos. Es decir, ponemos los números a sumar y los segundos que queremos que se retrase el programa   

import time

##Creamos la funcion con el time.sleep
def parandoTiempo (num1, num2, segundos):
    print("Estamos trabajando en ello, hemos visto tú numero "+str(num1)+ " y " +str(num2)+ " y con un retraso de " +str(segundos)+ " segundos")
    time.sleep(segundos)
    resultado = num1 + num2
    return resultado

#Creamos la opcion para añadir los datos
numero1 = int(input("Usuario, introduce el primer número: "))
numero2 = int(input("Usuario, introduce el segundo número: "))
segundosParados = int(input("¿Cuantos segundos quieres que tarde en salir dicho programa?: "))

resultadoFinal = parandoTiempo(numero1, numero2, segundosParados)

print("El resultado final de esta operacion, donde se suman " +str(numero1)+ " y " +str(numero2)+ " es igual a " +str(resultadoFinal))