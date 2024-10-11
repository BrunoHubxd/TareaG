#----------------------
tenis = 0
futbol = 0
totalEdadTenis = 0
totalEdadFutbol = 0

n = int(input("Ingrese la cantidad de socios: "))

for i in range(n):
    numSocio = int(input("Ingrese el número de socio: "))
    edad = int(input("Ingrese la edad: "))
    deporte = int(input("Ingrese el deporte: 1-Tenis, 2-Rugby, 3-Voley, 4-Hockey, 5-Futbol: "))

    if deporte == 1:
        tenis += 1
        totalEdadTenis += edad
    elif deporte == 5:
        futbol += 1
        totalEdadFutbol += edad

print(f"Cantidad de socios que practican tenis: {tenis}")
print(f"Cantidad de socios que practican fútbol: {futbol}")

if tenis > 0:
    print(f"Promedio de edad de jugadores de tenis: {totalEdadTenis / tenis:.2f}")

if futbol > 0:
    print(f"Promedio de edad de jugadores de fútbol: {totalEdadFutbol / futbol:.2f}")
#----------------------
