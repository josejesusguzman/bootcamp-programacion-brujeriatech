"""
Ludwingh28: Hey Sherp, una consulta podemos hacer un ejemplo que ordene una frase mediante punteros y burbujas? Pasa que en la Uni nos dieron un problema asi y con los for o se me dejaba a la mitad o me se me pasaba de vueltas 
"""

def bubble_sort(palabras) :

    for _ in range(len(palabras)) :
        palabras = list(palabras)

        for j in range(len(palabras) - 1) :
            if palabras[j] > palabras[j + 1] :
                palabras[j], palabras[j + 1] = palabras[j + 1], palabras[j]
        
    return palabras
    
frase = "de tal palo tal astilla"

palabras = frase.split()
palabras_ordenadas = [bubble_sort(palabra) for palabra in palabras]

print(palabras_ordenadas)