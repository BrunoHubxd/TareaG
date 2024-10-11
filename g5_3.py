# g5_3

# Crear una matriz de 40x5 para las notas de los alumnos
notas = [[0 for j in range(5)] for i in range(40)]

# Leer las notas de los 40 alumnos
for i in range(40):
    print(f"Ingrese las notas del alumno {i + 1}:")
    for j in range(5):
        notas[i][j] = float(input(f"Nota {j + 1}: "))

# Calcular y mostrar el promedio de cada alumno
for i in range(40):
    suma = sum(notas[i])
    promedio = suma / 5
    print(f"El promedio del alumno {i + 1} es: {promedio}")
