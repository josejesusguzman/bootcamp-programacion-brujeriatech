# zipfile
# Nos permite crear y leer archivos zip

import zipfile

# Crear un archivo zip
with zipfile.ZipFile("mi_comprimido.zip", "w") as archivo :
    archivo.write("documento.txt", arcname="documento.txt")

# Leer el archivo ZIP
with zipfile.ZipFile("mi_comprimido.zip", "r") as archivo :
    archivo.extractall("carpeta_descomprimida")