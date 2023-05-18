# Gestión de multiples excepciones

def funcion() :
    raise ExceptionGroup("Grupo1", [OSError(1), SystemError(2),
                            ExceptionGroup("Grupo2", [OSError(3), RecursionError(4)])])


try:
    funcion()
except* OSError as err:
    print("Hay OSError")
except* SystemError as err:
    print("Hay SystemError")
except* RecursionError as err:
    print("Hay RecursionError")

# NOTAS EN LAS EXCEPCIONES
try:
    raise TypeError("Mal tipo de dato")
except Exception as error:
    error.add_note("Es que pusiste entero en vez de flotante")
    error.add_note("Tas todo meco")
    error.add_note("Tu crush no te quiere")
    print(error)

def funcion1():
    raise OSError("Operación fallida")

problemas = []

for i in range(3) :
    try :
        funcion1()
    except Exception as error:
        error.add_note(f"Ocurrio en la iteración {i+1}")
        problemas.append(error)

raise ExceptionGroup("Tenemos problemas", problemas)
