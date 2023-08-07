#Crear una función que invierta el orden de los elementos en una lista dada.
def invertir_lista(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        
        lista[i], lista[longitud - i - 1] = lista[longitud - i - 1], lista[i]


numeros = input("Ingrese una lista de números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]

print("Lista original:", numeros)

invertir_lista(numeros)
print("Lista invertida:", numeros)