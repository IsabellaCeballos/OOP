#Escribir una función que calcule la media aritmética de una lista de números.
def media_aritmetica(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media
mi_lista = [10, 20, 30, 40, 50]
resultado_media = media_aritmetica(mi_lista)
print("La media aritmética de la lista es de:", resultado_media)
