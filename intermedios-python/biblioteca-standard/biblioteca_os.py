# la biblioteca os nos permite interactuar con el sistema operativo

import os

print(os.name)
print(os.getcwd())

try:
    os.mkdir("mi_carpeta.txt")
except FileExistsError:
    print("La carpeta ya existe. Intenta con otro nombre")


