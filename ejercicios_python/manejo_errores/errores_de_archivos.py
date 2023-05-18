import sys

try :
    archivo = open('D:\jose1\Documents\Innovaccion\clases-programacion-twitch\ejercicios_python\manejo_errores\\archivo.txt', "r")
    texto = archivo.readline()
    i = int(texto.strip())
except OSError as err :
    print("OSError:", err)
except ValueError:
    "No se pueden convertir los datos"
except Exception as err:
    print("Error no conocido:", err)
    raise
finally :
    archivo.close()

print(texto)
