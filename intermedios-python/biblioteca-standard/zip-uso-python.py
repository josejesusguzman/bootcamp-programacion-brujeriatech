# La función ZIP´
"""
Nos ayuda a combinar iterables  en un solo iterable
"""

nombres = ["Jesus", "Maria", "Jose", "Mari"]
edades = [30, 22, 19]
ciudades = ["Ciudad de México", "Lima", "Bogotá"]

combinado = list(zip(nombres, edades, ciudades))
print(combinado)

print("-------------------------------------------------")

for nombre, edad, ciudad in combinado :
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")