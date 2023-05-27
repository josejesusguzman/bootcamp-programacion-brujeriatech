"""
Verificar si un número es primo

A que solo sea divisible entre si mimo y el 1
Por ejemplo 7, 11

"""

def es_primo(numero) :
    if numero < 2 : # Uno y cero no son primos
        return False
    for i in range(2, int(numero**0.5) + 1) :
        if numero % i == 0 :
            print(numero, "/", i, "=", (numero / i))
            return False
    return True


print(es_primo(1000))


