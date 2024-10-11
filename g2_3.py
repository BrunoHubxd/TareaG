#----------------------
precio1 = float(input("Ingrese el precio por Kg del producto 1: "))
cantidad1 = float(input("Ingrese la cantidad en Kg adquirida del producto 1: "))

precio2 = float(input("Ingrese el precio por Kg del producto 2: "))
cantidad2 = float(input("Ingrese la cantidad en Kg adquirida del producto 2: "))

precio3 = float(input("Ingrese el precio por Kg del producto 3: "))
cantidad3 = float(input("Ingrese la cantidad en Kg adquirida del producto 3: "))

total1 = precio1 * cantidad1
total2 = precio2 * cantidad2
total3 = precio3 * cantidad3

totalCompra = total1 + total2 + total3

print("Monto total del producto 1:", total1)
print("Monto total del producto 2:", total2)
print("Monto total del producto 3:", total3)
print("Total de la compra:", totalCompra)

if totalCompra > 100:
    descuento = totalCompra * 0.10
    totalCompra -= descuento
    print("Nuevo monto con descuento del 10%:", totalCompra)
#----------------------
