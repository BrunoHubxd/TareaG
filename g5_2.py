# g5_2

# Crear una matriz de 4x4 inicializada en 0
matriz = [[0 for j in range(4)] for i in range(4)]

# Rellenar la diagonal con unos
for i in range(4):
    matriz[i][i] = 1

# Mostrar la matriz
for i in range(4):
    for j in range(4):
        print(matriz[i][j], end="")
    print()  # Salto de línea para la siguiente fila
