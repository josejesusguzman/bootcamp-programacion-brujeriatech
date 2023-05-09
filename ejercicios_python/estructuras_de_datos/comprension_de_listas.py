# List comprehension
# Es una manera concisa de crear listas

cuadrados = [] # Esta va a contener los números al cuadrado
for numero in range(10) :
    cuadrados.append(numero**2)
print(cuadrados)

cuadrados4 = []
def cuadrados_funcion(numero) :
    return numero * numero
for num in range(10) :
    cuadrados4.append(cuadrados_funcion(num))

print(cuadrados4)

cuadrados2 = list( map(lambda numero: numero**2, range(10)) )
print(cuadrados2)

cuadrados3 = [numero**2 for numero in range(10)]
print(cuadrados3)

from math import pi
print( [round(pi, i) for i in range(1, 6)] )

# Comprensión de listas anidadas

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10 , 11, 12]
]

print(matriz)

matriz1 = []
for i in range(4) :
    fila_matriz1 = []
    for fila in matriz :
        fila_matriz1.append(fila[i])
    matriz1.append(fila_matriz1)

print(matriz1)

matriz2 = []
for i in range(4) :
    matriz2.append([fila[i] for fila in matriz])

print(matriz2)

matriz3 = [ [fila[i] for fila in matriz] for i in range(4) ]
print(matriz3)

# Función o palabra reservada del

lista1 = [-1, 1, 4, 6, 4.44, 1000, 1256.51, 0, 4]

print(lista1)
print(lista1.pop(0))
print(lista1)

print(lista1.remove(4))
print(lista1)

del lista1[0]
print(lista1)

del lista1[3:]
print(lista1)

del lista1[:]
print(lista1)

del lista1
print(lista1)
