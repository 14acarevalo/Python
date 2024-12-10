#Ejercicio 1 - Crear una clase con atributos y métodos:

print("En este primer ejercicio, vamos a crear una clase conocida como coche y con varios atributos: ")

class Coche:
    def __init__(self, marca, modelo, año, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad
        
    def acelerar(self):
        self.velocidad = self.velocidad + 10
        return f"El coche ha acelerado, y ahora va a una velocidad de {self.velocidad} kms/h "
    
    def frenar(self):
        self.velocidad = self.velocidad - 10
        return f"El coche está frenando, y ahora va a una velocidad de {self.velocidad} kms/h "
    
    def mostrar_información(self):
        return f"Información sobre el vehículo:\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\nVelocidad actual: {self.velocidad} kms/h."


        

micoche = Coche("Opel", "Vectra", 1997, 110)
print(micoche.mostrar_información())
print("")
print(micoche.acelerar())
print("")
print(micoche.frenar())


#Ejercicio 2 - Crear una clase con atributos y métodos:

print("En este ejercicio, vamos a realizar una calculadora matemática: ")

class Calculadora:
    
    def __init__ (self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def sumar (self):
        return self.numero1 + self.numero2
    
    def restar (self):
        if (self.numero1 >= self.numero2):
            return self.numero1 - self.numero2
        else:
            return "No se puede obtener un valor negativo..."
    
    def multiplicar (self):
        return self.numero1 * self.numero2
    
    def dividir (self):
        if (self.numero1 >= self.numero2):
            return self.numero1 / self.numero2
        else:
            return "No se puede obtener un valor negativo..."
        
    def mostrar_informacion (self):
        return f" Numero 1: {self.numero1} - Numero 2: {self.numero2}"
    

numeros = Calculadora(7,5)

print ("Vamos a calcular las operaciones de nuestra calculadora: ")
print ("")
print(f"Mostramos información de los números elegidos: {numeros.mostrar_informacion()}")
print ("")
print(f"El resultado de la suma es: {numeros.sumar()}")
print(f"El resultado de la resta es: {numeros.restar()}")
print(f"El resultado de la multiplicacion es: {numeros.multiplicar()}")
print(f"El resultado de la division es: {numeros.dividir()}")
print ("")


    
#Ejercicio 3 - Trabajo con excepciones:

print ("En este ejercicio, vamos a crear una función y vamos a trabajar con excepciones")
def dividir (a, b):
    try:
        division = a/b
        return f"El resultado de dividir {a} entre {b} es igual a: {division}"
    except ZeroDivisionError:
        return "ERROR, no se puede dividir entre cero"

operacion = dividir (4,5)
print(operacion)
        
#Ejercicio 4 - Excepcion con archivos

print ("En este ejercicio, vamos a crear una función y vamos a trabajar con excepciones pero en este caso con archivos: ")

def leer_archivo():
    try:
        with open ('datos.txt') as archivo:
            print ("Leyendo archivo: ")
            print (archivo)
    except FileNotFoundError:
        return "ERROR, existe el archivo"

#Ejercicio 5 - Clases y métodos
print("En este ejercicio, continuamos con las clases y los métodos: ")

class Empleado:
    
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def aumentar_salario (self):
        self.salario = self.salario * 0.3 + self.salario
        return f"Tu aumento salario con el aumento es igual a {self.salario}"
    
    def mostrar_informacion (self):
        return f"Datos del empleado: \n Nombre: {self.nombre} \n Edad: {self.edad} \n Salario base: {self.salario}"

    
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, equipo_a_cargo):
        super().__init__(nombre, edad, salario) 
        self.equipo_a_cargo = equipo_a_cargo
        
    def añadir_a_equipo(self, nombre_empleado):
        self.nombre_empleado = nombre_empleado
        return f"El gerente ha contratado un nuevo empleado, el cual se llama {self.nombre_empleado}"
    
    def mostrar_informacion (self):
        return f"Datos del Gerente: \n Nombre: {self.nombre} \n Edad: {self.edad} \n Salario base: {self.salario} \n Equipo a cargo: {self.equipo_a_cargo}"

trabajador = Empleado("Alberto", 30, 1200)
print(trabajador.mostrar_informacion())
print(trabajador.aumentar_salario())

jefe = Gerente("Fernando", 61, 2000, "Construccion")
print(jefe.añadir_a_equipo("Pablo"))
print(jefe.mostrar_informacion())

#Ejercicio 6 - Clases y métodos (otro más)
import math

print("En este ejercicio vamos a trabajar para obtener el area de un circulo")
def calcular_area_circulo (radio):
    area = math.pi * radio**2
    return area

def calcular_volumen_cilindrico (radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base *altura
    return volumen

radio = 5
altura = 10

volumen = calcular_volumen_cilindrico (radio, altura)
print(f"El volumen de un cilindro con radio {radio} y altura {altura} es: {volumen}")    



        
    



