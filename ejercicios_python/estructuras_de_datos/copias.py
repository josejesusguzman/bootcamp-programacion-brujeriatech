# Copia superficial y copia profunda

import copy

lista1 = [1, 2, 3, [4, 5, [7]]]

# Esto es solo un copy paste de los valores pero las listas internas siguen ligadas
lista1_copia_superficial = lista1.copy()

# Aquí copias los valores y las listas internas se desligan, es como si redeclararas la variable
lista1_copia_profunda = copy.deepcopy(lista1)

lista1[3].append(6)
lista1[3][2].append(8)


print(lista1)
print(lista1_copia_superficial)
print(lista1_copia_profunda)