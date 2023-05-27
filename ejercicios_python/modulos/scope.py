# Scope o ámbito

# Ámbito local
def funcion() :
    variable_local = "Soy una variable local"
    print(variable_local)

funcion()

# Ámbito de cierre
def funcion_externa() :
    variable_cierre = "Soy una variable de cierre"

    def funcion_interna() :
        print(variable_cierre)

    funcion_interna()

funcion_externa()

# Ámbito global
variable_global = "Soy una variable global"

def funcion1() :
    print(variable_global)

funcion1()
print(variable_global)


# Ámbito incorporado
# No necesitamos declarar nada
print(len([1, 2, 3, 4, 0]))