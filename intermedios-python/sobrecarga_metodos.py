# Sobrecarga de métodos
# Python de manera nativa no soporta sobrecarga de métodos
# Pero podemos simularla

class Persona:
    def accion_recibida(self, insulto, golpe=None) :
        if golpe is None:
            print(f"Te han dicho {insulto}")
        else :
            print(f"Te han dicho {insulto} y además te golpearon")

jesus = Persona()
jesus.accion_recibida("chinga tu madre")
jesus.accion_recibida("puto", "GOLPE")

class MiClase :
    def mi_metodo(self, *args) :
        if len(args) == 1 :
            print(f"Hay un solo argumento: {args[0]}")
        elif len(args) == 2:
            print(f"Hay dos argumentos: {args[0]}, {args[1]}")
        else :
            print("No se han mandado argumentos o se ha sobrepasado el limite")

clase = MiClase()
clase.mi_metodo("1", "2", "sadsa")