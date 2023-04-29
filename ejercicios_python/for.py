# El ciclo for
"""
varias_palabras = []
num_palabras = 0

num_palabras = int(input("¿Cuantas palabras quieres ingresar? "))

# Si se necesita iterar sobre una secuencia de números usamos la función range()
# Range() generar números del cero al numero que especifiques -1

for i in range(num_palabras) :
    print("Palabra ", i + 1, " - Te quedan ", num_palabras - i - 1)
    palabra = input("Introduce la palabra: ")
    varias_palabras.append(palabra)

print("Este es el resultado")
print(varias_palabras)

"""
print("-----------------------------------------------------------------")

# Buscador de números primos
# Un número primo es el que solo se divide por si mismo y por 1

for n in range(2, 100) :
    es_primo = True
    for x in range(2, n) :
        if n % x == 0 :
            es_primo = False
            break
    if es_primo :
        print(n, "es número primo")



print("-----------------------------------------------------------------")
# CONTINUE
# Detector de pares e impares
for num in range(2, 10) :
    if num % 2 == 0 :
        print(num, "es par")  
        continue
    print(num, "es impar")