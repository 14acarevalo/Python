
##  Dado un listado de números, encuentra el SEGUNDO más grande

print("Usuario, vamos a calcular el segundo mayor ")
listaNumeros = [1,2,3,46,7,8,9,10,11,12,13,14,15,16]
mayor = 0
segundo_mayor = 0
for num in listaNumeros:
    if num>mayor:
        segundo_mayor = mayor
        mayor = num
    elif num>segundo_mayor and num != mayor:
        segundo_mayor = num
print("Mayor es igual a: " +str(mayor))
print("Segundo mayor es igual a: "+str(segundo_mayor))



 