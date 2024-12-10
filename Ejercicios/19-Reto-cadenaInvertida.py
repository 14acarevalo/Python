print("En este programa nos vamos a centrar en retornar las palabras con un orden invertido: ")
palabra = input("Usuario, escribe un string: ")
invertida = ""
print("Añadimos el ejemplo con las letras al revés, para que se vea en este ejemplo como se aplica el bucle for y en especial el orden de invertida: ")
for letra in palabra:
    invertida = letra+invertida
    print(invertida)
print(" ")
print("Alterando el orden de las letras, nos encontramos con: " +invertida)    
