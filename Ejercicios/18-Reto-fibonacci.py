print("En este reto, nos vamos a centrar el programa fibonacci, que consiste en una secuencia de números sumándose al anterior: ")
fibonacci = 0
anterior = 0
siguiente = 1
print("Sucesion Fibonacci: ")
for num in range (0, 51):
    fibonacci = anterior + siguiente
    anterior = siguiente
    siguiente = fibonacci
    print (fibonacci)
print("La secuencia de los números fibonacci, cuya suma ascienda a: " +str(fibonacci))