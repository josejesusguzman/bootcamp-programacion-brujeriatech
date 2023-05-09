tupla1 = (12345, 3.1416, "Hola", True )
lista1 = [12345, 3.1416, "Hola", True ]

super_tupla = tupla1, (1, 2, 3, 4, 5), [7, 8, 1]

print(super_tupla)

lista1[1] = 'c'
print(lista1)

super_tupla[2][0] = 'c'
print(super_tupla)

super_lista = list(super_tupla)
print(super_lista)

vacia = ()
# singleton
singleton_uwu = "Hola"
print(vacia) 
print(singleton_uwu)

