##En este reto, vamos a contar palabras
print("En este programa, vamos a contar las palabras que se pongan en tu frase")
frase = input("Dime algo bonito: ")
resultado = frase.split()
cantidad_palabras = len(resultado)
print(cantidad_palabras)