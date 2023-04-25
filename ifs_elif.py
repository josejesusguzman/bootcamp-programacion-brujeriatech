
tu_dinero = int(input('¿Cuanto traes? '))

edad = 19
cover = 100
costo_vip = 500
print("Edad:", edad)

if edad >= 18 and tu_dinero >= cover :
    tu_dinero = tu_dinero - cover
    print("\t\t Cobro de", cover)
    print("\tPasele al mamitas")
    print("\t¿Quiere un cigarro?")
    print("Tu dinero:", tu_dinero)
    if tu_dinero >= costo_vip :
        tu_dinero = tu_dinero - costo_vip
        print("\t\t Cobro de", costo_vip)
        print("\t Pasele al VIP")
        print("Tu dinero:", tu_dinero)
    else :
        print("\tNo puedes pasar al VIP, cuesta 500")