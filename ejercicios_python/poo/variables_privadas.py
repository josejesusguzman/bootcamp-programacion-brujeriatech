# Variables privadas

def esta_es_una_funcion() :
    return "esta_es_una_funcion"

class Mapping :

    def __init__(self, objeto_iterable) :
        self.lista = []
        self.__actualizar(objeto_iterable)

    def actualizar(self, obbjeto_iterable) : # Esta es una función privada
        for item in obbjeto_iterable :
            self.lista.append(item)

    __actualizar = actualizar # Actualizar es una variable privada 


class MappingSubClass(Mapping) :

    def actualizar(self, keys, values) :
        for item in zip(keys, values) :
            self.lista.append(item)

instancia = MappingSubClass(['a', 'b', 'c', 'd', 'e', 'f'])
instancia.actualizar(['key1'], ['value1'])
print(instancia.lista)

# EL ZIP
# Combina dos o más listas (o iterables) en una sola lista

numeros = [1, 2, 3, 4]
colores = ['rojo', 'verde', 'negro', 'azul', 'amarillo']
autos = ["Chevy", "Tsuru"]

combinados = zip(numeros, colores, autos)


for elemento in combinados :
    print(elemento)
