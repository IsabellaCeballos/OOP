#Crear un programa que genere una matriz de números y la imprima en pantalla
def generar_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    numero = 1
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = numero
            numero += 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


filas = int(input("Ingrese el número de las filas: "))
columnas = int(input("Ingrese el número de las columnas: "))


matriz_generada = generar_matriz(filas, columnas)
print("La matriz generada es:")
imprimir_matriz(matriz_generada)