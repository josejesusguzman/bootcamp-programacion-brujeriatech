# Polimorfismo
"""
- Métodos polimorficos
    Pemite que diferentes clases sean tratadas como instancias de la misma clase a través de la herencia

- isinstance() Devolver True si un objeto es una instancia de una clase

"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self) :
        print(f"{self.nombre} ladrando!!!!")
    
    def correr(self):
        print("Corre en cuatro patas")

class Gato(Animal) :
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self) :
        print(f"{self.nombre} maullando!!!!")

    def correr(self):
        print("Corre en cuatro patas")

class Persona(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print(f"{self.nombre} te está mentando la madre!!!!")

    def correr(self):
        print("Corre en dos patas")


def sonido_animal(animal):
    animal.hacer_sonido()

def correr(animal):
    animal.correr()

brujita = Gato("brujita", "Calico")
jesus = Persona("Jesus")
sonido_animal(brujita)
correr(brujita)
sonido_animal(jesus)
correr(jesus)
