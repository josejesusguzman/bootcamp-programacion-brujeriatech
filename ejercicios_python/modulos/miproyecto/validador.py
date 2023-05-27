

# Este es el sistema de validación de edad de expedición de licencias en CDMX
def puedes_conducir(edad = 0) :

    if edad < 15 : 
        return False
    elif edad >= 15 and edad < 18 :
        return True, "Provisional"
    elif edad >= 18 and edad < 80 :
        return True, "Normal"
    else :
        return False
    

def tipo_licencia(tipo_vehiculo = "automovil") :

    match tipo_vehiculo :
        case "automovil":
            return "A"
        case "motocicleta" :
            return "A1"
        case "taxi" :
            return "B"
        case _:
            return False
        
