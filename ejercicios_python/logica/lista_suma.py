"""
De una lista encuentra el par que sume un número que le des
Que devuelva los dos núimeros que suman el número objetivo

[1, 2, 3]
Objetivo= 3
Resultado = 1, 2
"""

def buscar(lista, objetivo) :
    visto = {}
    for num in lista :
        if objetivo - num in visto:
            return [objetivo - num, num]
        visto[num] = True
    return []

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(buscar(lista_numeros, objetivo=17))