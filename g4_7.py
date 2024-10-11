# Inicializamos la cantidad de camiones que cargaron té
camionesConTe = 0

# Procesamos los datos de los 30 camiones
for i in range(30):
    print(f"Ingrese la patente del camión {i + 1}:")
    patente = input()
    print(f"Ingrese el nombre del chofer del camión {i + 1}:")
    nombreChofer = input()
    print(f"Ingrese el apellido del chofer del camión {i + 1}:")
    apellidoChofer = input()
    print("Ingrese el tipo de carga (madera, yerba, té):")
    tipoCarga = input()
    print(f"Ingrese la hora de egreso del camión {i + 1}:")
    horaEgreso = input()

    if tipoCarga.lower() == "té":
        camionesConTe += 1

    print(f"Datos del camión {i + 1}:")
    print(f"Patente: {patente}")
    print(f"Chofer: {nombreChofer} {apellidoChofer}")
    print(f"Carga: {tipoCarga}")
    print(f"Hora de egreso: {horaEgreso}")
    print("------------------------")

# Mostramos la cantidad de camiones que cargaron té
print(f"Cantidad de camiones que cargaron té: {camionesConTe}")
