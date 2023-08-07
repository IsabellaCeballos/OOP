#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no
def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = ''.join(c for c in cadena if c.isalnum()) 
    return cadena == cadena[::-1]


cadena = input("Ingrese una cadena de texto: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")