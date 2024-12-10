##Vamos a parar el tiempo con este ejercicio

import time

def suma (num1, num2, segundos):
    print("Usuario, dado los números introducidos " +str(num1)+ " y " +str(num2)+ " más el retraso de " +str(segundos)+ " segundos... vamos a realizar una operación")
    time.sleep(segundos)
    resultado = num1 + num2
    return resultado

print("Usuario, en este programa se busca introducir numeros y retrasar su suma los segundos que tu digas ")
numero1 = int(input("Usuario, introduce un primer número: "))
numero2 = int(input("Usuario, introduce un segundo número: "))
segundos1 = int(input("¿Cuántos segundos quieres retrasar la operación?: "))

resultado1=suma(numero1, numero2, segundos1)

print(f"El resultado final de realizar la suma entre {numero1} y {numero2} es igual a {resultado1} y con un retraso de {segundos1} ")