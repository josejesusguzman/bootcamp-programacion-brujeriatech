# Acciones de limpieza
# Buena práctica

while True:
    try :
        file = open("testfile.txt", "w")
        edad = int(input("Coloca tu edad: "))
        file.write("Tu edad al cuadrado es: " +  str(edad ** 2))
        print("Se ha escrito en el archivo con éxito")
        break
    except KeyboardInterrupt:
        print("\nEl usuario ha detenido el programa")
        break
    except IOError:
        print("Hubo un error al escribir un archivo")
    except ValueError("Usuario") as error:
        print("No introduzcas letras, solo números")
    finally: 
        file.close()

print("Adios, vuelve pronto")