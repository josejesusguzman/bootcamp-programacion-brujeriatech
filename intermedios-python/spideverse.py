class Spiderman :

    # Picadura de araña
    def __init__(self) :
        print("Spiderman original picado por la araña")
    
    def lanzar_telaraña(self) :
        print("Lanza telaraña")
    
    def activar_sentido_aracnido(self, peligro):
        if peligro :
            print("Se activa el sentido aracnido")
        else :
            print("No pasa nada")

class MilesMorales(Spiderman) :

    def __init__(self):
        print("Miles Morales lo pica una araña")

    def lanzar_telaraña(self):
        print("Necesita aditamentos")
        return super().lanzar_telaraña() # Usa la función de la clase padre
    
    def lanzar_rayitos(self):
        print("Lanza rayito")

class SpiderGwen(Spiderman):
    def __init__(self):
        print("A Gwen Stacy la pica una araña")

    def lanzar_telaraña_rosa(self):
        print("La talaraña es rosa")
        return super().lanzar_telaraña() # Usa la función de la clase padre
    
class Spidercito(MilesMorales, SpiderGwen) :

    def __init__(self):
        print("Porque hicieron el delicioso")
        super().lanzar_rayitos() # Esta función viene de Miles, el padre
    
miles = MilesMorales()
miles.lanzar_telaraña()

gwen = SpiderGwen()
gwen.lanzar_telaraña_rosa()

spidercito = Spidercito()
spidercito.lanzar_telaraña_rosa() # Esta función viene de Gwen, la madre

spidercito.activar_sentido_aracnido(peligro=True)

print(isinstance(spidercito, Spiderman))