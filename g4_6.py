# Inicializamos el total
precioTotal = 0

# Pedimos la cantidad de productos
n = int(input("Ingrese la cantidad de productos: "))

# Inicializamos los vectores
cantidades = [0] * n
costos = [0] * n

# Cargamos las cantidades y costos de los productos
for i in range(n):
    cantidades[i] = int(input(f"Ingrese la cantidad del producto {i + 1}: "))
    costos[i] = float(input(f"Ingrese el costo del producto {i + 1}: "))
    precioTotal += cantidades[i] * costos[i]

# Mostramos el precio total
print(f"El precio total es: {precioTotal}")

# Mostramos los productos que superan los $1000
print("Productos que superan los $1000:")
for i in range(n):
    if (cantidades[i] * costos[i]) > 1000:
        print(f"Producto {i + 1} con costo: {cantidades[i] * costos[i]}")

