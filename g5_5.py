# g5_6

# Crear la matriz de 4x4 (4 alumnos y 4 columnas: 3 notas + promedio)
matriz = [[0 for j in range(4)] for i in range(4)]

# Cargar las notas y calcular el promedio
for i in range(4):
    suma = 0
    for j in range(3):
        matriz[i][j] = float(input(f"Ingrese la nota {j+1} del alumno {i+1}: "))
        suma += matriz[i][j]
    
    # Calcular y guardar el promedio en la última columna
    promedio = suma / 3
    matriz[i][3] = promedio

# Mostrar la matriz con las notas y los promedios
print("               Nota 1   Nota 2   Nota 3   Promedio")
for i in range(4):
    print(f"Alumno {i+1}: ", end="")
    for j in range(4):  # Recorrer las 4 columnas (3 notas + promedio)
        print(f"{matriz[i][j]:.2f}", end="\t")  # Formato con dos decimales y tabulación
    print()  # Salto de línea para cada alumno
