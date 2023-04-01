# Tipos de datos
dato = "5" # Una cadena de caracteres o string o cadena de texto
print(dato + dato)
dato = 5 # númerico - Entero sin decimales
print(dato + dato)
dato = 5.0 # númerico - Flotante - Con punto decimal
print(dato + dato)
dato = False # Booleano - Verdero o falso - True o False
print(dato + dato)

# La función exit cierra el programa de python
print("💖")
print("你好世界")
exit()

cinco = "5"
numero = 5

# Solución 1: Comvertir el valor
print(float(cinco) + numero)


# Solución 2: Formato de cadenas
nombre = "Jesús"
edad = 27
# El objetivo es imprimir: Hola, mi nombre es Jesús y tengo 27 años
print('Hola, mi nombre es {} y tengo {} años'.format(nombre, edad))

# Solución 3 f-string
print(f'Hola, mi nombre es {nombre} y tengo {edad} años')

# Solución  1 de nuevo: Cast del dato - con concatenación
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años")


print(__name__)
