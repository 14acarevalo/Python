##En este ejercicio, vamos a realizar la búsqueda de anagramas introduciendo palabras

def es_palindromo (palabra):
         return palabra == palabra[::-1]
    
    
palabra1 = input("Usuario, introduce una palabra: ")
palabra2 = input("Usuario, introduce otra palabra: ")


if es_palindromo(palabra1):
    print("Esta palabra se lee igual empieces por donde empieces...")
else:
    print("Esta palabra va a su aire...")
    
    
if es_palindromo(palabra2):
    print("Esta palabra se lee igual empieces por donde empieces...")
else:
    print("Esta palabra va a su aire...")
    
    

