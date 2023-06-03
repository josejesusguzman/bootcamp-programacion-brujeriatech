import random

# Para 10,000 numeros tarda: 00:09:35
def metodo_burbuja(lista) :
    n = len(lista)

    cambio = True

    while cambio:
        # Creamos una bandera
        cambio = False

        for i in range(n - 1) :
            if lista[i] > lista[i + 1] :
                lista[i], lista[i + 1 ] = lista[i + 1], lista[i]
                cambio = True

    return lista

lista_aleatoria = [ random.randint(0, 100) for _ in range(10000) ]
print(lista_aleatoria)

print(metodo_burbuja(lista_aleatoria))