# Errores y excepciones

tu_edad = 0

while True :
    try:
        tu_edad = int(input("¿Qué edad tienes?"))
        break
    except ValueError:
        pass
        

print(tu_edad)

class A(Exception) :
    pass

class B(A):
    pass

class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print("Error de tipo C")
    except B :
        print("Error de tipo B")
    except A:
        print("Error de tipo A")


try:
    raise Exception("perro", "Gato")
except Exception as error :
    print(type(error))
    print(error.args)
    print(error)

    x, y = error.args
    print("x=", x)
    print("y=", y)