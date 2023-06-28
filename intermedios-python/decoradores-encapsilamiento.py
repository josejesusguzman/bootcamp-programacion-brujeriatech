# DECORADORES Y ENCAPSULAMIENTO
"""
Un DECORADOR es una función que toma otra función y extiemnde su funcionalidad sin modificar explicitamente su comportamiento

ENCAPSULAMIENTO: Es que una variable o atributo de clase o de instancia solo puedan ser accedidos por medio de métodos conocidos como GETTERS Y SETTERS

"""
import numpy as np

class Circulo :
    def __init__(self, radio):
        self._radio = radio

    # Getter de radio
    @property # Me ayuda a poder llamar a un método como si fuese una variable cualquiera
    def radio(self):
        return self._radio
    
    # Setter de radio
    @radio.setter
    def radio(self, valor) :
        if valor < 0 :
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def diametro(self):
        return self._radio * 2
    
    @property
    def area(self):
        return np.pi * self._radio ** 2
    

mi_circulo = Circulo(5)
print(mi_circulo.radio)
print(mi_circulo.diametro)
print(mi_circulo.area)


mi_circulo.radio = 10
print(mi_circulo.radio)
print(mi_circulo.diametro)
print(mi_circulo.area)