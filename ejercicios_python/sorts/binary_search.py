

def busqueda_binaria(lista, x):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high :
        mid = (high + low) // 2

        if lista[mid] < x :
            low = mid + 1
        elif lista[mid] > x :
            high = mid - 1
        else :
            return mid
    
    return -1

lista = [2, 5, 6, 7, 90, 110]
x = 2

resultado = busqueda_binaria(lista, x)

if resultado != -1 :
    print("El elemento está en el indice", resultado)
else:
    print("El elemento no se encuentra en la lista")