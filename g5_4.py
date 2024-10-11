# g5_4

# Crear la matriz CANT de 50x15 para las ventas de los artículos por los vendedores
CANT = [[0 for j in range(15)] for i in range(50)]

# Crear el vector TOTAL para almacenar las ventas totales por cada vendedor
TOTAL = [0 for j in range(15)]

# Cargar la matriz CANT con las ventas y sumar en el vector TOTAL
for i in range(50):
    for j in range(15):
        CANT[i][j] = int(input(f"Ingrese la cantidad del artículo {i+1} vendida por el vendedor {j+1}: "))
        TOTAL[j] += CANT[i][j]  # Sumar la venta al total del vendedor

# Buscar el vendedor con la mayor venta
maxVenta = TOTAL[0]
vendedorMax = 1

for j in range(1, 15):
    if TOTAL[j] > maxVenta:
        maxVenta = TOTAL[j]
        vendedorMax = j + 1

# Mostrar el vendedor con la mayor venta
print(f"El vendedor que realizó la mayor venta es el número: {vendedorMax} con un total de {maxVenta} artículos vendidos.")
