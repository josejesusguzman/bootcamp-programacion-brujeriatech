#  Administrador de Table 
tu_dinero = int(input('¿Cuanto dinero traes? '))
edad = int(input("¿Cuantos años tienes? "))

cover = 100
costo_vip = 500
print("Edad:", edad)

if edad >= 18 and tu_dinero >= cover :
    tu_dinero = tu_dinero - cover
    print("\t\t Cobro de", cover)
    print("\tPasele al mamitas")
    print("\t¿Quiere un cigarro?")
    print("Tu dinero:", tu_dinero)
    vip = int(input("¿Quieres pasar al VIP? 1:Sí - 2:No "))
    if vip == 1 and tu_dinero >= costo_vip :
        tu_dinero = tu_dinero - costo_vip
        print("\t\t Cobro de", costo_vip)
        print("\t Pasele al VIP")
        print("Tu dinero:", tu_dinero)
    elif vip == 1 and tu_dinero < costo_vip:
        print("\t No te alcanza. Largate")
        print("Tu dinero:", tu_dinero)
    elif vip == 2 :
        print("\t No se preocupe, siga disfrutando del mamitas")
        print("Tu dinero:", tu_dinero)
elif edad < 18 :
    print("Tas muy verde, vete a ver Pocoyo")
else:
    print("Ere pobre, vete")
