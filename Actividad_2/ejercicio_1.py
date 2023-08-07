#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehículo:
    
    def __init__(self, vel_maxima, kilometraje):
        self.vel_maxima = vel_maxima
        self.kilometraje = kilometraje

vehiculo = Vehículo(230, 10000)
print("La Velocidad máxima es:", vehiculo.vel_maxima)
print("El Kilometraje es:", vehiculo.kilometraje)
