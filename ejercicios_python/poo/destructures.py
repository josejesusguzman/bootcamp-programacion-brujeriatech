class Archivo :
    def __init__(self, nombre_archivo) :
        self.archivo = open(nombre_archivo, 'w')

    def __del__(self) :
        self.archivo.close()

archivo_instancia = Archivo("ejercicios_python\poo\ejemplo.txt")
archivo_instancia.archivo.write("No es brujería, es tecnología")
del archivo_instancia
