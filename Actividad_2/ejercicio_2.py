#Cree una clase Punto que represente un punto en el plano cartesiano.
#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.


import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
    
    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)


punto1 = Punto(6, 5)
punto2 = Punto(4, 9)

punto1.mostrar()
punto2.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia)
