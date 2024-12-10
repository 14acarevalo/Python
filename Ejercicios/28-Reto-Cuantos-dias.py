##Vamos a crear un programa que calcule cuantos la diferencia de dias de dentro de un mes

dia1 = int(input("Usuario, introduce un día del 1 al 31: "))
mes1 = int(input("Usuario, introduce el mes: "))
año1 = int(input("Usuario, introduce el año: "))

print("¿Tú fecha es el " +str(dia1)+"/"+str(mes1)+"/"+str(año1)+ " ? ")
respuesta = input("Pulsa S en caso afirmativo o N en caso negativo: ")

if respuesta == "S":
    print("Usuario, vamos con la segunda fecha")
    dia2 = int(input("Usuario, introduce un día del 1 al 31: "))
    mes2 = int(input("Usuario, introduce el mes: "))
    año2 = int(input("Usuario, introduce el año: "))
        
    if mes1==mes2 and año1==año2:
        resultado = dia2-dia1
        print("La diferencia entre estos dias es de: " +str(resultado))
    elif mes1==mes2 and año1!=año2:
        print("Los años son diferentes...")
    elif mes1!=mes2 and año1==año2:
        print("Los meses son diferentes...")

else:
    print("Hemos cometido un error al mostrarte la fecha por pantalla, lo lamentamos")
            
###########################################################################################

from datetime import datetime

def es_fecha_valida(dia, mes, año):
    try:
        fecha = datetime(año, mes, dia)
        return True
    except ValueError:
        return False

dia1 = int(input("Usuario, introduce un día del 1 al 31: "))
mes1 = int(input("Usuario, introduce el mes: "))
año1 = int(input("Usuario, introduce el año: "))

if es_fecha_valida(dia1, mes1, año1):
    print(f"¿Tu fecha es el {dia1}/{mes1}/{año1}?")
    respuesta = input("Pulsa S en caso afirmativo o N en caso negativo: ").upper()

    if respuesta == "S":
        print("Usuario, vamos con la segunda fecha")
        dia2 = int(input("Usuario, introduce un día del 1 al 31: "))
        mes2 = int(input("Usuario, introduce el mes: "))
        año2 = int(input("Usuario, introduce el año: "))

        if es_fecha_valida(dia2, mes2, año2):
            if mes1 == mes2 and año1 == año2:
                resultado = abs(dia2 - dia1)
                print(f"La diferencia entre estos días es de: {resultado} días")
            else:
                print("Los meses o años son diferentes. Por favor, introduce fechas dentro del mismo mes y año.")
        else:
            print("La segunda fecha no es válida. Por favor, revisa los valores introducidos.")
    else:
        print("Hemos cometido un error al mostrarte la fecha por pantalla, lo lamentamos.")
else:
    print("La primera fecha no es válida. Por favor, revisa los valores introducidos.")
