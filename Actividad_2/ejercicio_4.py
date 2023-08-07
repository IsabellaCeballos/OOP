#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. 
#Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Círculo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def cal_area(self):
        return math.pi * self.radio**2
    
    def cal_perímetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_al_centro <= self.radio


centro = Punto(5, 9)
circulo = Círculo(centro, 2)

area = circulo.cal_area()
print("El Área del círculo es:", area)

perímetro = circulo.cal_perímetro()
print("El Perímetro del círculo es:", perímetro)

punto = Punto(3, 2)
if circulo.punto_pertenece(punto):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")
