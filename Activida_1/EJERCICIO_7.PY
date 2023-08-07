#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

numeros = input("Ingrese una lista de números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]

# Inicializar las variables para el número más grande y más pequeño
maximo = numeros[0]
minimo = numeros[0]

# Encontrar el número más grande y más pequeño
for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print("El número ingresado mas grande es:", maximo)
print("El número ingresado mas pequeño es:", minimo)