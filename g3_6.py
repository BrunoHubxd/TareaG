#----------------------
mejorTiempo = 0
mejorVehiculo = 0

for i in range(12):
    vehiculo = int(input("Ingrese el número del vehículo: "))
    tiempo = int(input("Ingrese el tiempo (en segundos): "))

    if i == 0 or tiempo < mejorTiempo:
        mejorTiempo = tiempo
        mejorVehiculo = vehiculo

print(f"Mejor tiempo: {mejorTiempo}")
print(f"Número de vehículo: {mejorVehiculo}")
#----------------------
