# Algoritmo para calcular la nota más alta y el promedio
n = int(input("Ingrese la cantidad de notas: "))
vector = [0] * n  # Definir un vector de tamaño n

suma = 0
notaMax = 0

for i in range(n):
    vector[i] = float(input(f"Ingrese la nota {i + 1}: "))
    suma += vector[i]
    
    if vector[i] > notaMax:
        notaMax = vector[i]

promedio = suma / n
print("La nota más alta es:", notaMax)
print("El promedio de notas es:", promedio)
