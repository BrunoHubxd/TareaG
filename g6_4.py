# Función que determina si un año es bisiesto
def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("Es año bisiesto.")
                return True
            else:
                print("No es año bisiesto.")
                return False
        else:
            print("Es año bisiesto.")
            return True
    else:
        print("No es año bisiesto.")
        return False

# Solicitar un año al usuario
año = int(input("Ingrese un año: "))

# Verificar y mostrar si el año es bisiesto
es_bisiesto(año)
