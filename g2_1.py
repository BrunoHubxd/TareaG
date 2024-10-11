#----------------------
categoria = int(input("Ingresa la categoría del empleado (1-repositor, 2-cajero, 3-supervisor): "))

if categoria == 1:
    sueldbruto = 32335
    bono = sueldbruto * 0.08
elif categoria == 2:
    sueldbruto = 38630.89
    bono = 0
elif categoria == 3:
    sueldbruto = 45560.20
    bono = 0
else:
    print("Categoría inválida")
    exit()

descJ = sueldbruto * 0.11
descOS = sueldbruto * 0.03

sueldN = sueldbruto - (descJ + descOS)

print("Sueldo Bruto:", sueldbruto)
print("Descuento por Jubilación:", descJ)
print("Descuento por Obra Social:", descOS)
print("Sueldo Neto:", sueldN)

if bono > 0:
    print("Bono en compras para repositores:", bono)
#----------------------
