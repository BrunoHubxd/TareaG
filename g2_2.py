#----------------------
cantidad = int(input("Ingrese la cantidad de paquetes: "))

if cantidad < 5:
    print("No se permiten compras inferiores a 5 productos.")
else:
    if cantidad >= 5 and cantidad <= 15:
        print("El costo de envío es de $200.")
    else:
        print("El envío es gratuito.")
#----------------------
