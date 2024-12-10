## Es una copia del archivo 38-Clases y objetos



##En esta tarea, lo que se busca es trabajar, aprender y mejorar sobre clases y objetos en python
#Tarea 3 de CAMPUS ATRIUM


## 1) Crear una clase básica con atributos y métodos básicos
#Escribe un programa en Python para crear una clase Vehicle con atributos de instancia __max_speed__ y __mileage__. 
#Y 2 métodos:
#<ul>
#    <li>get_max_speed()</li>
#    <li>increase_mileage(ammount_to_increase)</li>
#</ul>
print("Ejercicio 1: En este ejercicio, se va a crear una clase para valorar la velocidad de un vehiculo y la distancia recorrida:")

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def get_max_speed (self):
        return self.max_speed
    
    def increase_mileage(self, incremento_kilometros):
        self.mileage = self.mileage + incremento_kilometros
    
##A modo de ejemplo:

vehiculo = Vehicle(120, 100)
print(f"El vehiculo va a una velocidad maxima de {vehiculo.max_speed} kilometros/hora")
print(f"El vehiculo ha recorrido una distancia de {vehiculo.mileage} kilometros")

vehiculo.increase_mileage(234)
print(f"Al aumentar la velocidad ha sido capaz de recorrer una distancia de {vehiculo.mileage} kilometros")
print("")

## 2) Crear una clase con atributos y métodos
#Escribe una clase __Rectangle__ en lenguaje Python, que te permita construir un rectángulo con atributos de longitud y anchura.
#Crea un método __perimeter()__ para calcular el perímetro del rectángulo y un método __area()__ para calcular el área del rectángulo.
#Crear un método __display()__ que muestre la longitud, la anchura, el perímetro y el área de un objeto creado mediante una instanciación de la clase rectángulo.
#Sobrescribir el método \_\_str\()\_\_ para que la representación de la cadena por defecto de la clase sea la definida en display()
print("Ejercicio 2: En este ejercicio, se va a crear una clase rectangulo para trabajar con diferentes atributos y métodos de este:")

class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura
    
    def perimeter(self):
        return 2*(self.longitud+self.anchura)
    
    def area(self):
        return self.longitud*self.anchura
        
    def display(self):
        print(f"La longitud es igual a: {self.longitud}")
        print(f"La anchura es igual a: {self.anchura}")
        print(f"El perimetro es igual a: {self.perimeter()}")
        print(f"El área es igual a: {self.area()}")
        
    def __str__(self):
        return (f"LOS DATOS DE MI RECTANGULO SON:\n" 
                f"LONGITUD: {self.longitud}\n"
                f"ANCHURA {self.anchura}\n"
                f"PERIMETRO {self.perimeter()}\n"
                f"AREA {self.area()}")
    
rectangulo = Rectangle(4,2)
print(f"El perimetro del rectangulo es igual a {rectangulo.perimeter()}")
print(f"El area del rectangulo es igual a {rectangulo.area()}")
print("")
print("Los datos del rectángulo, son los siguientes: ")
print(rectangulo.display())
print(rectangulo)
print("")
## 3) Crear una clase más avanzada con atributos y métodos
#Crea una clase de Python llamada __BankAccount__ que represente una cuenta bancaria, teniendo como atributos 
#<ul>
#<li> <b>account_number</b> (de tipo numérico), <b>name</b> (nombre del titular de la cuenta, string), <b>balance</b>.</li>
#</ul>
#Y con los siguientes métodos:
#<ul>
#<li>Crear un constructor con parámetros: <b>account_number</b>, <b>name</b>, <b>balance</b>.</li>
#<li>Crear un método <b>deposit(ammount)</b> que gestione las acciones de depósito.</li>
#<li>Crear un método <b>withdrawal(ammount)</b> que gestione las acciones de retirada.</li>   
#<li>Crear un método <b>transfer(acc_to_transfer_to_obj, ammount)</b> que transfiera dinero a otro objeto de cuenta bancaria que reciba como parámetro.</li>
#<li>Crear un método <b>apply_bank_fees(percentage)</b> que aplique las comisiones bancarias con un porcentaje del saldo actual de la cuenta.</li>
#<li>Crear un método <b>display()</b> para mostrar los detalles de la cuenta.</li>
#</ul>
#Implementar también los métodos necesarios para comparar diferentes cuentas bancarias por saldo utilizando los operadores > < >= <= y ==.
                
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit (self, ammount):
        if ammount > 0:
            self.balance = self.balance + ammount
            print (f"Tienes un saldo de {ammount} y un balance de {self.balance}")
        else:
            print("Tu saldo se corresponde con 0 €")
    
    def withdrawal(self, ammount):
        if ammount > 0:  # Verifico que la cantidad a retirar es positiva
            if self.balance >= ammount:  # Compruebo que hay suficiente saldo para el retiro
                self.balance -= ammount  # Resto el monto solicitado del saldo
                print(f"Retiro exitoso de {ammount} €. Nuevo saldo: {self.balance} €")
            else:
                print(f"La cantidad solicitada no está disponible. Te faltarían {ammount - self.balance} €.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")
    
    def transfer (self, acc_to_transfer_to_obj, ammount):
        if ammount > 0:
            if self.balance >= ammount:
                if isinstance (acc_to_transfer_to_obj, BankAccount):
                    self.balance = self.balance - ammount
                    acc_to_transfer_to_obj.balance = acc_to_transfer_to_obj.balance + ammount
                    print(f"Transferencia realizada con exito, hemos añadido {ammount} € y tienes un nuevo saldo, {self.balance} €")
                else:
                    print("No se ha podido realizar la transferencia deseada")
            else:
                print("No tienes suficiente dinero para hacer frente al saldo")
        else: 
            print("No tienes dinero en la cuenta, 0 € para ser exactos")   
    
    def apply_bank_fees(self,percentage):
        if percentage > 0 and percentage < 5:
            fee = self.balance*(percentage/100)
            print(f"Con el porcentaje actual {percentage}%, tienes un balance de: {fee}")     
            self.balance = self.balance - fee
            print(f"Tu nuevo saldo se corresponde con: {self.balance}")
        else:
            print("El porcentaje no entra dentro de nuestras posibilidades bancarias")
    
    def display (self):
        print (f"El número de la cuenta es: {self.account_number}")     
        print (f"El nombre de la cuenta es: {self.name}")  
        print (f"El balance de la cuenta es: {self.balance}")   
        
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __eq__(self, other):
        return self.balance == other.balance
    


    
 
v1 = [4,3,8,1]
v2 = [9,2,7,3]
producto = 0
for i, j in zip(v1,v2):
    
    producto += i*j
    print(producto) 