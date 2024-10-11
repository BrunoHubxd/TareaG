#----------------------
dni = input("Ingrese el DNI del empleado: ")
categoria = int(input("Ingrese la categoría del empleado (0-Maestranza, 1-Administración, 2-Gerencia): "))

if categoria == 0:
    sueldbruto = 23600
    descJ = sueldbruto * 0.11
    descOS = sueldbruto * 0.03
    descClub = 0
    nombreCat = "Maestranza"
elif categoria == 1:
    sueldbruto = 35800
    descJ = sueldbruto * 0.11
    descOS = sueldbruto * 0.05
    descClub = 0
    nombreCat = "Administración"
elif categoria == 2:
    sueldbruto = 60420
    descJ = sueldbruto * 0.11
    descOS = sueldbruto * 0.05
    descClub = sueldbruto * 0.04
    nombreCat = "Gerencia"
else:
    print("Categoría inválida")
    exit()

sueldN = sueldbruto - (descJ + descOS + descClub)

print("DNI:", dni)
print("Categoría:", nombreCat)
print("Sueldo Neto:", sueldN)
#----------------------
