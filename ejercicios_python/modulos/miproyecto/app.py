import validador as vl

edad = 0

while True :
    try :
        edad = int(input("Coloca tu edad: "))
        break
    except ValueError :
        print("Edad incorrecta, intenta nuevamente")

if vl.puedes_conducir(edad) :
    print("Puedes conducir")
    vehiculo = input("¿Qué tipo de vehiculo maneja: (automovil, moticicleta o taxi): ")
    tipo = vl.tipo_licencia(vehiculo)
    if tipo :
        print("Licencia", tipo)
    else :
        print("Ese tipo de auto no existe")
else :
    print("NO PUEDES CONDUCIR")