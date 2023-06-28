# Composición
"""
Construiis clases más complejas utilizando objetos de ot7ras clases
"""

# Clase más chiquita
class Motor :
    def iniciar(self):
        motor_iniciado = True
        print("Motor iniciandose")
        return motor_iniciado

class CajaVelocidades:
    def cambiar_velocidad(self, subir=False):
        if subir :
            print("Se ha subido la marcha")
        else :
            print("Se ha bajado la marcha")

# Carro es la clase más compleja
class Carro :
    def __init__(self):
        self.motor_iniciado = False
        self.motor = Motor()
        self.velocidades = CajaVelocidades()

    def iniciar_motor(self) :
        self.motor_iniciado = self.motor.iniciar()

    def cambiar_marcha(self, subir=False) :
        if self.motor_iniciado :
            self.velocidades.cambiar_velocidad(subir)
        else :
            print("Primero debes encender el coche")

mi_coche = Carro()

mi_coche.iniciar_motor()
mi_coche.cambiar_marcha(True)
