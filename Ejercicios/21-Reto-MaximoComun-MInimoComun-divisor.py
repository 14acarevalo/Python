##Crea una funcion donde se busque calcular el MCD


def MCD (num1, num2):
    if num1 >= num2:
        while num2 !=0:
            division = num1%num2   
            num1 = num2
            num2 = division
        return num1 
        
print("Usuario, introduce unos números y vamos a calcular el maximo común divisor ")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Usuario, introduce el segundo número: "))

resultado = MCD (numero1, numero2)

print(f"El maximo común divisor de los números  {numero1} y {numero2} es igual a {resultado} ")
    