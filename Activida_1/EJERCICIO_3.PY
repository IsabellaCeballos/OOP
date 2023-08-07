#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

longitud = int(input("Ingrese el tamaño de la lista: "))
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))

lista_aleatoria = []

for _ in range(longitud):
    numero_aleatorio = minimo + int(random.random() * (maximo - minimo + 1))
    lista_aleatoria.append(numero_aleatorio)

print("Lista de números aleatorios:")
for numero in lista_aleatoria:
    print(numero)