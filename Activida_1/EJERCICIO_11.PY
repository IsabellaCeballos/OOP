#Crear un programa que genere una lista de números pares entre 1 y 100.
def generar_lista_par():
    lista_par = [numero for numero in range(2, 101) if numero % 2 == 0]
    return lista_par

lista_pares_generada = generar_lista_par()
print("La lista de números pares entre 1 y 100 es:")
print(lista_pares_generada)