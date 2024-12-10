##
  #Crea un programa que imprima los 30 próximos años bisiestos
  #siguientes a uno dado.
  #Utiliza el menor número de líneas para resolver el ejercicio.
  
año = int(input("Usuario, introduce el año en el que estás y añadieremos los próximos 30 años: "))
for num in range (año, (año+31)):
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        print ("El año " +str(num)+ " es bisiesto!!!!!!!!!!!!!!")
    else:
        print("Año " +str(num)+ " no es bisiesto")
        
print(" ")
        
##
  #Crea una funcion que imprima los 30 próximos años 
  #siguientes a uno dado.
  #Utiliza el menor número de líneas para resolver el ejercicio.
  
def añoBisiesto(año1):
    for num in range (año1, (año1+31)):
        if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
            print ("El año " +str(num)+ " es bisiesto!!!!!!!!!!!!!!")
        else:
            print("Año " +str(num)+ " no es bisiesto")

año1 = int(input("Usuario introduce un año: "))
print(añoBisiesto(año1))

print(" ")

##
  #Crea una funcion que imprima los 30 próximos años bisiestos
  #siguientes a uno dado.
  #Utiliza el menor número de líneas para resolver el ejercicio.

def añoBIsiesto1(año2):
    for num in range(año2, (año2+201)):
        if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
            print(str(num))
            
año2 = int(input("Usuario, introduce un año: "))
print(añoBIsiesto1(año2))