class Figura : # Esta sería la clase padre
    """
    Define una figura según su base y altura
    """

    def __init__(self, base, altura) :
        self.base = base
        self.altura = altura

class Poligono :

    def dar_nombre(self, nombre) :
        return f"Esto es un {nombre}"

class Rectangulo(Figura, Poligono) :

    def calcular_area(self) : # Este es un método
        return self.base * self.altura
    


class Triangulo(Figura) :

    def calcular_area(self) :
        return (self.base * self.altura) // 2
    
rectangulo = Rectangulo(20, 5)
triangulo = Triangulo(20, 20)

print("Área del rectangulo:",  rectangulo.calcular_area())
print("Área del triangulo:", triangulo.calcular_area())

print(rectangulo.dar_nombre("Rectangulo"))
