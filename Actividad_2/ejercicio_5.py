#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor).
# Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
    
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TRÉBOLES = "Tréboles"
    PICAS = "Picas"
    
    def __init__(self, valor, pinta):
        self.Cvalor = valor
        self.Cpinta = pinta

carta = Carta(5, Carta.DIAMANTES)
print("El Valor de la carta:", carta.Cvalor)
print("La Pinta de la carta:", carta.Cpinta)
