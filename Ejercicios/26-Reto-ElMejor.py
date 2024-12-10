##Vamos a crear un programa en donde se busque saber quien es el mejor

alberto = [10, 8.2, 9, 5, 6, 7.2, 8.9]
pablo = [7,8, 9.5, 8.5, 9.7, 7, 7, 6]

def media(numero):
    resultado = sum(numero)/len(numero)
    return resultado

media_usuario1=media(alberto)
media_usuario2=media(pablo)

print("En este programa tenemos 2 participantes, uno de ellos Alberto (primer participante) y en segundo lugar, Pablo (segundo participante), ambos han realizado 7 lanzamientos y han obtenido diferentes puntuanciones. ¿Quién ganará?")
print("El resultado del primer concursante es igual a: " +str(media_usuario1))
print("El resultado del segundo concursante es igual a: " +str(media_usuario2))

if media_usuario1>media_usuario2:
    print("El primer concursante tiene mejor media")
else:
    print("El segundo concursante tiene mejor media")