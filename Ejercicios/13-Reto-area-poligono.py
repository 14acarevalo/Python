##
 # Crea una única función (importante que sólo sea una) que sea capaz
 # de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Imprime el cálculo del área de un polígono de cada tipo.
base = 0
altura = 0

def areaPoligono () :
    area = base*altura
    return area
    
print("Usuario, vamos a calcular el área de tu polígono ")
base = float(input("Usuario introduce la base: "))
altura = float(input("Usuario introduce la altura de tu poligono: "))
resultado = areaPoligono()
print("El área de tu poligono es igual a : " +str(resultado))