#Ejercicio 1: Introducción a la herencia
#Objetivo: Crear una clase base y una clase derivada que herede atributos.
#Crea una clase Animal con un atributo nombre y un método hablar(). Luego, crea una clase Perro que herede de Animal y sobrescriba el método hablar() para que el perro ladre.
print("Ejercicio 1:")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        return "El animal esta hablando"

class Perro(Animal):
    def hablar(self):
        return "Grrrr"
    
mi_perro = Perro("Rex")
print (f"El perro {mi_perro.nombre} esta diciendo {mi_perro.hablar()}")

#Ejercicio 2: Uso de super()
#Objetivo: Reutilizar métodos de la clase base en la clase derivada.
#Extiende el ejercicio anterior usando super() para invocar el método hablar() de la clase Animal en la clase Perro. Además, añade otra clase Gato que también sobrescriba el método hablar().
print("Ejercicio 2:")

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comunicar(self):
        return "algo ¿qué será?"

class Perro(Animales):
    def comunicar(self):
        return f"{super().comunicar() } Grrrr"

class Gato(Animales):
    def comunicar (self):
        return "MIaou"
    
mi_perro = Perro("Rex")
mi_gato = Gato("Junior")
print (f"El perro {mi_perro.nombre} esta diciendo {mi_perro.comunicar()}")
print (f"El gato {mi_gato.nombre} esta diciendo {mi_gato.comunicar()}")

#Ejercicio 3: Añadir atributos específicos
#Objetivo: Añadir atributos propios de la clase derivada.
#Crea una clase Vehiculo con atributos como marca y velocidad_maxima. Luego, crea una clase Coche que herede de Vehiculo y tenga un atributo adicional numero_puertas.
print("Ejercicio 3:")

class Vehiculo:
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
    
class Coche(Vehiculo):
    def __init__(self, marca, velocidad_maxima, numero_puertas):
        super().__init__(marca, velocidad_maxima)
        self.numero_puertas = numero_puertas
        
    def info(self):
        return f"El vehiculo, cuya marca es {self.marca} va a una velocidad de {self.velocidad_maxima} km/h y tiene {self.numero_puertas} puertas"

mi_coche = Coche ("Opel", 120, 5)
print(mi_coche.info())

#Ejercicio 4: Sobrescribir métodos de la clase padre
#Objetivo: Sobrescribir métodos de la clase base y agregar lógica adicional.
#Crea una clase Empleado con un método calcular_salario(). Luego, crea una clase Gerente que sobrescriba el método para agregar un bono adicional al salario.
print("Ejercicio 4:")

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
        
    def calcular_salario(self):
        return self.salario_base
    
    
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, plus):
        super().__init__(nombre, salario_base)
        self.plus = plus
        
    def calcular_salario(self):
        return super().calcular_salario() + self.plus
    
empleado = Empleado("Alberto", 1200)
gerente = Gerente("Pablo", 2000, 500)

print(f"El empleado con nombre {empleado.nombre} tiene un salario base de {empleado.calcular_salario()}")
print(f"El gerente con nombre {gerente.nombre} tiene un salario base de {gerente.calcular_salario()} ya que esta formado por {gerente.salario_base} € y un plus de {gerente.plus} €")


#Ejercicio 5: Múltiples niveles de herencia
#Objetivo: Implementar herencia con múltiples niveles.
#Crea una clase Persona, una clase Empleado que herede de Persona, y una clase Gerente que herede de Empleado. Cada clase debe añadir atributos y métodos adicionales.
print("Ejercicio 5:")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    
    def info (self):
        return f"El empleado con nombre {self.nombre} tiene {self.edad} años y un salario de {self.salario} € al mes"
    
class Gerente (Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
        
    def info (self):
        return f"El gerente con nombre {self.nombre} tiene {self.edad} años y un salario de {self.salario} € al mes pertenece al departamento {self.departamento}"


persona = Persona("Alberto", 30)
empleado = Empleado ("Pablo", 22, 1500)
gerente = Gerente("Fernando", 61, 2300, "recursos informaticos")

print (f"Hola, me llamo {persona.nombre} y tengo {persona.edad} años")
print (f"Hola, me llamo {empleado.nombre} y tengo {empleado.edad} años y un salario de {empleado.salario} € al mes")
print (f"Hola, me llamo {gerente.nombre}, tengo {gerente.edad} años y un salario de {gerente.salario} € al mes, mas elevado que el empleado {empleado.nombre} porque trabajo en el departamento de {gerente.departamento}")


#Ejercicio 6: Uso de polimorfismo
#Objetivo: Implementar polimorfismo en la herencia.
#Crea una clase base Figura con un método area() que devuelva 0. Luego, crea clases derivadas Cuadrado y Círculo, y sobrescribe el método area() para devolver el área correcta según la figura.

import math

class Figura:
    def __init__(self) -> None:
        pass
    
    def area(self):
        return 0
    
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        
    def area(self):
        return self.lado**2
    
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        
    def area(self):
        return (self.radio**2)*math.pi
    
cuadrado = Cuadrado(4)
circulo = Circulo(3)

print(f"El área del cuadrado es: {cuadrado.area()}")
print(f"El área del círculo es: {circulo.area()}")