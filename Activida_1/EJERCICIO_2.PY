#Escribir una función que calcule el área de un círculo dado su radio
def calcular_area_circulo(radio):
    area = 3.141592653589793 * (radio ** 2)
    return area

radio_circulo = (int(input("Ingrese el radio del circulo al cual se le calculara el area ")))
area_circulo = calcular_area_circulo(radio_circulo)
print("El área del círculo corresponde a:", area_circulo)