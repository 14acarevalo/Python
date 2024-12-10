##En este programa vamos a crear una opcion que nos permita conocer el segundo mayor de una lista de números

print("En este programa vamos a sacar el mayor y segundo mayor de una lista de números ")

def segundoMayor(lista):
    mayor = float('-inf')
    segundo_mayor = float('-inf')
    if len(lista) <= 2:
        print("La lista es demasiado pequeña ")
    else:
        for numero in lista:
            if numero > mayor:
                segundo_mayor=mayor
                mayor = numero
            elif numero > segundo_mayor and numero != mayor:
                segundo_mayor = numero
        return segundo_mayor

lista = [1,2,3,4,5,6,7,8,9,14,21,22]       
resultado = segundoMayor(lista)

print(f"El resultado de esta lista, donde nos encontramos el segundo mayor es igual a: {resultado}")
        
        
           
            
