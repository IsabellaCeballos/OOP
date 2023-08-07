#Escribir una función que calcule el factorial de un número dado.
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")