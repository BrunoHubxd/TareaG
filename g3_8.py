#----------------------
cantTotal = 0
cantHombres = 0
cantMujeres = 0
cantHombresJovenes = 0
maxEdad = -1
docMayorEdad = 0

doc = int(input("Ingrese el número de documento (0 para finalizar): "))

while doc != 0:
    cantTotal += 1
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (F o M): ").upper()

    if sexo == 'M':
        cantHombres += 1
        if 16 <= edad <= 65:
            cantHombresJovenes += 1
    else:
        cantMujeres += 1

    if edad > maxEdad:
        maxEdad = edad
        docMayorEdad = doc

    doc = int(input("Ingrese el número de documento (0 para finalizar): "))

print(f"Cantidad total de personas censadas: {cantTotal}")
print(f"Cantidad de hombres censados: {cantHombres}")
print(f"Cantidad de mujeres censadas: {cantMujeres}")

if cantHombres > 0:
    porcentajeHombresJovenes = (cantHombresJovenes * 100) / cantHombres
    print(f"Porcentaje de hombres entre 16 y 65 años: {porcentajeHombresJovenes:.2f}%")

print(f"Mayor edad registrada: {maxEdad} con número de documento: {docMayorEdad}")
#----------------------
