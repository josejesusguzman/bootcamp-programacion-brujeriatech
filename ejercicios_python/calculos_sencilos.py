print( 2 + 2 )
print( (50 - 5*9) / 4)

impuesto = 16 / 100 # 16%
precio = 31149.30 # Precio de laptop

precio * impuesto

# Ejemplo de operador ternario
esta_dormido = False
status = "Esta dormido" if esta_dormido else "No esta dormido"
print(status)


# Cadenas de caracteres 

print('They\'ve said "I\'m Crazy"') # They've said "I'm Crazy"
print("They've said \"I'm Crazy\"") # They've said "I'm Crazy"

print("Hola \n Mundo")
print('C:\algun\nombre')
print('C:\\algun\\nombre')
print(r'C:\algun\nombre')


"""
ESTO ES UN COMENTARIO MULTILINEA
PUEDO PONER VARIAS LINEAS DE COMENTARIO
"""
print("""
Hola soy Jesús
    -h          Obten ayuda de la aplicación
    -H url      Hackea a la url dada
""")

print(3 * 'o' + 'x')
print(2 * 'xo')

print('Py' 'thon')
print('Py', 'thon') # Aquí si te pone un espacio

# Texto muy largo en print
print("El oso bailaba sobre la luna mientras las vacas saltaban en la montaña."
    "El sol brillaba con una luz roja y verde, y los pájaros cantaban en un idioma"
    "desconocido. Los árboles se movían al ritmo de la música, y las piedras bailaban"
    "con los caracoles. Todo era una fiesta sin fin, "
    "y las flores lanzaban confeti al aire.")

palabra = "Python" # Esto también puede funcionar como una lista

print(palabra[0]) # Siempre me va a dar el primer eqlemento
print(palabra[5]) 
print(palabra[-1])
print(palabra[-2])
print(palabra[-3])

# Obtener los dos primeros caracteres
print(palabra[0] + palabra[1])
print(palabra[0:2])
print(palabra[2:5])
print(palabra[2:])

print(len(palabra))

print(palabra[0:2] + palabra[2])

print(palabra[0:2+1])