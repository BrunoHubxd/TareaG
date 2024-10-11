#----------------------
for i in range(5):
    dni = int(input("Ingrese el DNI del cliente: "))
    tipoServ = int(input("Ingrese el tipo de servicio: 1-30M, 2-50M, 3-100M: "))

    if tipoServ == 1:
        monto = 750
    elif tipoServ == 2:
        monto = 1100
    else:
        monto = 1500 * 0.95

    print(f"DNI: {dni}")
    print(f"Monto a pagar: {monto}")
    print(f"Tipo de servicio: {tipoServ}")
#----------------------
