# Encadenamiento de excepciones

def funcion():
    raise ConnectionError

try :
    funcion()
except ConnectionError as error :
    raise RuntimeError("No se puede manejar el error") from error