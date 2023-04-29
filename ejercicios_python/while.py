# Ciclo while
# Mientras la condición se cumpla, seguira haciendo el ciclo 

contador = 0

# Esto es un ciclo infinito
"""
while True:
    print("Este es un ciclo infinito", contador)
    contador = contador + 1 
"""

# El pass no hace nada pero se usa para no dejar algo vacio y no tener error de sinatxis
class Vacia:
    pass

numero = 7
while True :
    pregunta = int(input("Adivina el número: "))
    if pregunta == numero :
        break

print("Has adivinado correctamente")

# La función EVAL
cadena = "contador + 4"
resultado = eval(cadena)
print(resultado)

