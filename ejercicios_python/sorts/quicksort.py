import random

# Para 100,000 numeros tarda: 00:03:00
def metodo_quicksort(lista) :
    if len(lista) <= 1 :
        return lista
    else :
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]

        return metodo_quicksort(menores) + iguales + metodo_quicksort(mayores)


lista_aleatoria = [ random.randint(0, 100) for _ in range(1000000) ]
print(lista_aleatoria)

print(metodo_quicksort(lista_aleatoria))