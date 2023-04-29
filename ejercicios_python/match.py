# Estructura match, es como el switch case de otros lenguajes
# Evalua una variable y da el resultado y se detiene cuando encuentra una coincidencia

status = 403

match status :
    case 400 :
        print("Bad request")
    case 401 | 403 | 405 :
        print("Client error")
    case 404 :
        print("Not found")
    case 418 :
        print("I'm a teapot")
    case _: # Este es el default o lo que pasa cuando las condiciones anteriores no se cumplen
        print("Pus nose")