# Herencia simple
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):

    # Variable de clase
    especie = "Canis Familiaris"

    def __init__(self, nombre, raza):
        # Esto es una variable de instancia porque se declara en el constructor y solo la puedes usar a nivel de instancia
        super().__init__(nombre)

        if not isinstance(nombre, str):
            raise ValueError("El nombre del perro debe ser un string")
        
        if not isinstance(raza, str):
            raise ValueError("La raza del perro debe ser un string")

        self.__raza = raza # Esta es una variable pública

    # GETTERS & SETTERS
    
    # Este es el getter nombre del perro - Puede obtener el nombre del perro
    def get_raza(self) :
        return self.__raza
    
    # Este es el setter del nombre pero - Puede cambiar el nombre del perro
    def set_raza(self, nombre) :
        self.__raza = nombre

    def ladrar(self) :
        print(f"{self.nombre} ladra!!!! WOF WOF")



puppy = Perro("Puppy", "Crestado") # Método de instancia
manchas = Perro("Manchas", "Schnauzer")

print(puppy.nombre)
print(puppy.get_raza())
puppy.set_raza("Corriente")
print(puppy.get_raza())
print(manchas.get_raza())
print(Perro.especie)
print(puppy.especie)
manchas.ladrar()


# Herencia Múltiple



