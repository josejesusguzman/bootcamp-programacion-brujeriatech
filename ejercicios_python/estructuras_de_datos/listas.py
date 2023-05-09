# Lista

lista = [1, 2, 3, 4, 5, 6.7, "ocho", 9, False, 1]

print(lista)

"""
#Esto no jala porque está comentado
for cada_elemento in lista :
    print(cada_elemento)
"""
    
# Añade un elemento al final de la lista
print("Append")
lista.append(55)
print(lista)

# Extiende la lista agregandole ottra lista u otro iterable al final
print("Extend")
lista2 = [0, True, "cero", "0"]
lista.extend(lista2)
print(lista)

# Insertar un elemento en una posición que le des
print("Insert")
lista.insert(2, 2.5)

print(lista)

# Quitar el primer elemento que encuentre con ese valor
print("Remove")
lista.remove(0)
lista.remove(0)
print(lista.remove('0'))

print(lista)

# Quita el elemento en la posición que le des y lo retorna
print("pop")

print(lista.pop(-1))
elemento_eliminado = lista.pop(0)
print(elemento_eliminado)

print(lista)

# Devolver el indice del primer elemento que sea igual al que le mandemos
print("Index")
print(lista.index(2.5))
print(lista.index(3, 2, 4))

# Realizar una copia superficial de una lista - Podemos editar la nueva lista
print("Copy")

lista_copia = lista
lista_medio_metro = lista.copy()

lista_medio_metro.pop()

lista.append(5)

print(lista_copia)
print(lista)
print(lista_medio_metro)

# Contar cuantas veces el elemento aparece en la lista
print("Count")

lista.append(3)
print(lista)
print(lista.count(33))

# Ordenar los elementos de una lista
print("Sort")

lista.remove("ocho")

print(lista)
lista.sort()
print(lista)

lista_palabras = ["Mojo", 'Python', 'PHP', 'Java', 'ADA', 'C', 'JavaScript', 'COBOL']
print(lista_palabras)
lista_palabras.sort()
print(lista_palabras)

# Invertir la lista
print("Reverse")
print(lista)
lista.reverse()
print(lista)

# Elimina todos los elementos de la lista
print("Clear")

lista.clear()

# del lista

print(lista)
