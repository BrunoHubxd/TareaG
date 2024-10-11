# Definimos el cambio de dólares a pesos
cambio = 140

# Inicializamos los vectores
vendedores = [0] * 15
ventas = [0] * 15

# Cargamos las ventas de los vendedores
for i in range(15):
    ventas[i] = float(input(f"Ingrese la venta del vendedor {i + 1}: "))
    vendedores[i] = i + 1

# Inicializamos las posiciones del vendedor con la mayor y menor venta
posMax = 0
posMin = 0

# Encontramos el vendedor con la mayor y menor venta
for i in range(15):
    if ventas[i] > ventas[posMax]:
        posMax = i
    if ventas[i] < ventas[posMin] or posMin == 0:
        posMin = i

# Mostramos los resultados
print(f"El vendedor con la mayor venta es: {vendedores[posMax]}")
print(f"Venta en dólares: {ventas[posMax]}")
print(f"Venta en pesos: {ventas[posMax] * cambio}")

print(f"El vendedor con la menor venta es: {vendedores[posMin]}")
print(f"Venta en dólares: {ventas[posMin]}")
print(f"Venta en pesos: {ventas[posMin] * cambio}")
