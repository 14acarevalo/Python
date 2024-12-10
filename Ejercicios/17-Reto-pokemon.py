##
 # Crea un programa que calcule el daño de un ataque durante
 # una batalla Pokémon.
 # - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 # - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 # - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 #   (buscar su efectividad)
 # - El programa recibe los siguientes parámetros:
 #  - Tipo del Pokémon atacante.
 #  - Tipo del Pokémon defensor.
 #  - Ataque: Entre 1 y 100.
 #  - Defensa: Entre 1 y 100.
def calcular_efectividad(tipo_atacante, tipo_defensor):
    efectividad = {
        ('Agua', 'Fuego'): 2,
        ('Agua', 'Planta'): 0.5,
        ('Agua', 'Eléctrico'): 1,
        ('Fuego', 'Planta'): 2,
        ('Fuego', 'Agua'): 0.5,
        ('Fuego', 'Eléctrico'): 1,
        ('Planta', 'Agua'): 2,
        ('Planta', 'Fuego'): 0.5,
        ('Planta', 'Eléctrico'): 1,
        ('Eléctrico', 'Agua'): 2,
        ('Eléctrico', 'Planta'): 0.5,
        ('Eléctrico', 'Fuego'): 1,
    }
    return efectividad.get((tipo_atacante, tipo_defensor), 1)

def calcular_daño(ataque, defensa, efectividad):
    return 50 * (ataque / defensa) * efectividad

# Solicitar datos al usuario
print("Usuario, vamos a jugar a los Pokémon, necesito saber unos datos sobre tu Pokémon:")
tipo_atacante = input("Tipo del Pokémon atacante (Agua, Fuego, Planta, Eléctrico): ")
tipo_defensor = input("Tipo del Pokémon defensor (Agua, Fuego, Planta, Eléctrico): ")
ataque = int(input("¿Cuánto ataque tiene tu Pokémon? (Entre 1 y 100): "))
defensa = int(input("¿Cuánta defensa tiene el Pokémon enemigo? (Entre 1 y 100): "))

# Calcular efectividad y daño
efectividad = calcular_efectividad(tipo_atacante, tipo_defensor)
daño = calcular_daño(ataque, defensa, efectividad)

print(f"El daño causado por {tipo_atacante} a {tipo_defensor} es de: {daño:.2f}")
