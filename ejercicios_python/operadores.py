# Operadores aritméticos
numero1 = 5
numero2 = 10
numero3 = "5"
numero4 = "5"

# Operador de suma / concatenación
print("------------ SUMA --------------")
print(numero1 + numero2)
print(numero3 + numero4)

# Operador de resta

print("------------ RESTA --------------")
print(numero1 - numero2)
# print(numero3 - numero4) # Esto no se puede hacer

print("------------ MULTIPLICACIÓN --------------")
print(numero1 * numero2)

print("------------ DIVISIÓN --------------")
print(numero2 / numero1)

# El operador modulo nos devuelve el residuo de una división entera
print("------------ MODULO --------------")
print(numero2 % numero1)

# POTENCIA DE UN NÚMERO
# N cantidad de veces un número multiplicado por si mismo
print("------------ POTENCIA --------------")
print(2 ** 3)
print(numero2 ** numero1)

# División entera
# Te hace la división pero el resultado es sin punto decimal
print("------------ DIVISIÓN --------------")
print(numero2 // numero1)

# Operadores relacionales

# Mayor que
# Devuelve True si el número de la izquierda es MAYOR QUE el número de la derecha
print("------------ MAYOR QUE --------------")
print(numero1 > numero2)

# Menor que
# Devuelve True si el número de la izquierda es MENOR QUE el número de la derecha
print("------------ MENOR QUE --------------")
print(numero1 < numero2)

# Operador igualdad

print("------------ IGUAL QUE --------------")
print(numero1 == numero2)
print(5 == 5)
print(5 == "5")
print(5 == 5.0) # Datos flotantes y enteros los trata como numericos

# Operador MAYOR O IGUAL QUE
print("------------  MAYOR O IGUAL QUE --------------")
# Nos da True si el valor de la izquierda es mayor o igual al de la derecha
print(numero2 > numero1)
print(numero1 == numero2)
print(numero2 >= numero2)
print(numero2 >= numero1)

# Operador MENOR O IGUAL QUE
print("------------  MENOR O IGUAL QUE --------------")
# Nos da True si el valor de la izquierda es MENOR O IGUAL QUE el de la derecha
print(numero2 < numero1)
print(numero1 == numero2)
print(numero2 <= numero2)
print(numero2 <= numero1)
print(numero1 <= numero2)

# Operador de desigualdad

print("------------  ES DIFERENTE QUE --------------")
# Nos da True si ambos valores no son iguales o son diferentes
print(numero1 != numero2)
print(5 != 5)
print(5 != "5")
print(5 != 5.0) # Datos flotantes y enteros los trata como numericos

# Operadores bit a bit 
a = 2 # En binario: 10
b = 3 # En binario: 11 

# Operador AND BIT A BITu operación AND EN BINARIOS  
print("------------  AND BIT A BIT --------------")
print(a & b)

# Operador OR BIT A BIT u operación OR EN BINARIOS
print("------------  OR BIT A BIT --------------")
print(a | b)

# Operador XOR BIT A BIT 
print("------------  XOR BIT A BIT --------------")
print(a ^ b)

# Operador NOT BIT A BIT 
print("------------  NOT BIT A BIT --------------")
# Invertir cada bit en el operando
# Este es un operador de solo un número

print(~a) # -3

# DESPLAZAMIENTO A LA DERECHA
print("------------  DESPLAZAMIENTO A LA DERECHA --------------")
print(a >> b)

# DESPLAZAMIENTO A LA IZQUIERDA
print("------------  DESPLAZAMIENTO A LA IZQUIERDA --------------")
print(a << b)
print(b << a)


# --- OPERADORES LOGICOS -----
print("------------  OPERADORES LÓGICOS --------------")
print("------------  OPERADOR LÓGICO AND --------------")
costo_cigarros = 50
dinero = 7
edad = 7
print((dinero >= costo_cigarros) and (edad >= 18))
print(True and False)

print("------------  OPERADOR LÓGICO OR --------------")
costo_cigarros = 50
dinero = 7
edad = 70
print((dinero >= costo_cigarros) and (edad >= 18))
print(False or True)

print("------------  OPERADOR LÓGICO NOT --------------")
costo_cigarros = 50
dinero = 7
edad = 70
print(not ((dinero >= costo_cigarros) and (edad >= 18)))
print(not False)
print(not True)

# Operadores de pertenencia

print("------------  OPERADORES PERTENENCIA --------------")
print("------------  OPERADOR IN --------------")

lista = [1, 2, 3, 4, 5]

# in  -> Pertence a - esta en
print(3 in lista)
print(7 in lista)

# not in  -> NO pertenece a - NO esta en
print("------------  OPERADOR NOT IN --------------")

print(3 not in lista)
print(7 not in lista)

# Operadores de identidad
print("------------  OPERADORES IDENTIDAD --------------")
print("------------  OPERADOR IS --------------")

a = 3
b = 3
c = 4
d = a

print (a is b)
print (a is d)
print (a is c)

print("------------  OPERADOR IS NOT --------------")
print (a is not b)
print (a is not d)
print (a is not c)

a = a + a
print(a)
print(d)

