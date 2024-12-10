
# En este programa se va a convertir el tiempo en milisegundos
print("Bienvenido a la máquina del tiempo, aquí vamos a convertir el tiempo que introduzcas en milisegundos. ¡Vamos allá!")

def conversor(dia):
    conversionDia = dia * 86400000
    return conversionDia

def conversorH(horas):
    conversionHoras = horas * 3600000
    return conversionHoras

def conversorM(minutos):
    conversionMinutos = minutos * 60000
    return conversionMinutos

def conversorS(segundos):
    conversionSegundos = segundos * 1000
    return conversionSegundos

# Solicitar entrada del usuario
dia = int(input("Usuario, ¿cuántos días vamos a transformar?: "))
horas = int(input("Usuario, ¿cuántas horas vamos a transformar?: "))
minutos = int(input("Usuario, ¿cuántos minutos vamos a transformar?: "))
segundos = int(input("Usuario, ¿cuántos segundos vamos a transformar?: "))

# Realizar las conversiones
resultadoDia = conversor(dia)
resultadoHoras = conversorH(horas)
resultadoMinutos = conversorM(minutos)
resultadoSegundos = conversorS(segundos)

# Calcular el total en milisegundos
total = resultadoDia + resultadoHoras + resultadoMinutos + resultadoSegundos
print(" ")
# Mostrar los resultados
print("Tus días dan como resultado: " + str(resultadoDia) + " milisegundos")
print("Tus horas dan como resultado: " + str(resultadoHoras) + " milisegundos")
print("Tus minutos dan como resultado: " + str(resultadoMinutos) + " milisegundos")
print("Tus segundos dan como resultado: " + str(resultadoSegundos) + " milisegundos")
print(" ")
print("El tiempo total es igual a: " + str(total) + " milisegundos")
