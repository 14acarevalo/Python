##Vamos a crear un programa donde el sombre seleccionador nos diga a que pertenecemos:

contadorGryffindor = 0
contadorSlythering = 0
contadorRavenclaw = 0
contadorHupplefud = 0

def casaMagica(contadorGryffindor, contadorSlythering, contadorRavenclaw, contadorHupplefu):
    if contadorGryffindor > contadorSlythering and contadorGryffindor > contadorHupplefud and contadorGryffindor > contadorRavenclaw :
        print("Eres de Gryffyndor!!!!!")    
    elif contadorGryffindor < contadorSlythering and contadorSlythering > contadorHupplefud and contadorSlythering > contadorRavenclaw :
        print("Eres de Slythering!!!!!")    
    elif contadorRavenclaw > contadorSlythering and contadorRavenclaw > contadorHupplefud and contadorGryffindor < contadorRavenclaw :
        print("Eres de Ravenclaw!!!!!")    
    elif contadorHupplefud > contadorSlythering and contadorGryffindor < contadorHupplefud and contadorHupplefud > contadorRavenclaw :
        print("Eres de Gryffyndor!!!!!")   
    elif contadorGryffindor == contadorHupplefud or contadorGryffindor == contadorRavenclaw or contadorGryffindor == contadorSlythering or contadorSlythering == contadorRavenclaw or contadorSlythering == contadorRavenclaw :
        print("Tenemos que definirte un poco más, tienes un poco de varias casas...") 
        
        
        

print("Bienvenido joven mago a Hogwarts, te haré unas preguntas para saber a la casa a la que vas a pertenecer ")
print("Vamos allá!!!!! ")
print("Joven mago, ¿de las siguientes caracteristicas ¿Cómo te defines?")
print(" ")
print("A) Valiente")
print("B) Leal")
print("C) Curioso")
print("D) Ambicioso")
print(" ")
respuesta = input("Elige opcion, A, B, C o D: ")
if respuesta == "A":
    contadorGryffindor +=1
elif respuesta == "B":
    contadorHupplefud +=1
elif respuesta == "C":
    contadorRavenclaw +=1
elif respuesta == "D":
    contadorSlythering +=1
else:
    print("Por favor, escoge una opcion valida")
print(" ")

print("Joven mago, tenemos otra pregunta para ti, ¿de las siguientes caracteristicas ¿Cuál se asemeja más a ti?")
print(" ")
print("A) Atrevido")
print("B) Trabajador")
print("C) Inteligente")
print("D) Astuto")
print(" ")
respuesta = input("Elige opcion, A, B, C o D: ")
if respuesta == "A":
    contadorGryffindor +=1
elif respuesta == "B":
    contadorHupplefud +=1
elif respuesta == "C":
    contadorRavenclaw +=1
elif respuesta == "D":
    contadorSlythering +=1
else:
    print("Por favor, escoge una opcion valida")
print(" ")

print("Joven mago, tenemos más preguntas para ti, ¿de las siguientes caracteristicas ¿Cuál se asemeja más a ti?")
print(" ")
print("A) Decidido")
print("B) Curioso")
print("C) Leal")
print("D) Respetuoso")
print(" ")
respuesta = input("Elige opcion, A, B, C o D: ")
if respuesta == "A":
    contadorGryffindor +=1
elif respuesta == "B":
    contadorHupplefud +=1
elif respuesta == "C":
    contadorRavenclaw +=1
elif respuesta == "D":
    contadorSlythering +=1
else:
    print("Por favor, escoge una opcion valida")
print(" ")

print("Joven mago, tenemos una última pregunta para ti, ¿de las siguientes caracteristicas ¿Cuál se asemeja más a ti?")
print(" ")
print("A) Defensor de los débiles")
print("B) Innovador")
print("C) Honesto")
print("D) Lider")
print(" ")
respuesta = input("Elige opcion, A, B, C o D: ")
if respuesta == "A":
    contadorGryffindor +=1
elif respuesta == "B":
    contadorHupplefud +=1
elif respuesta == "C":
    contadorRavenclaw +=1
elif respuesta == "D":
    contadorSlythering +=1
else:
    print("Por favor, escoge una opcion valida")
print(" ")


casaMagica(contadorGryffindor, contadorSlythering, contadorRavenclaw, contadorHupplefud)

