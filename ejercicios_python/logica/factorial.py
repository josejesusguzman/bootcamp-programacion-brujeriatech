"""
FACTORIAL DE UN NÚMERO

ERs un número no negativo "n!" es el producto de 
todos los números enteros positivos de 1 hasta n

La multiplicación de todos los números desde 1 hasta n

factorial de 5 = 5*4*3*2*1 = 120

El factorial de 0 y de 1 es 1

"""

# Recursión
def factorial(numero) :
    if numero == 0 or numero == 1 :
        return 1
    else :
        print(numero, "*", (numero - 1), "=", numero * (numero - 1))
        return numero * factorial(numero - 1)
    
print(factorial(6))


# Con lambda y reduce
from functools import reduce

def factorial_masoquista(numero):
    if numero == 0 or numero == 1 :
        return 1
    else :
        return reduce(lambda x, y: x * y, range(1, numero+1))
    

numeros = [10, 4, 12]
factoriales = list(map(factorial_masoquista, numeros))

print(factoriales)
