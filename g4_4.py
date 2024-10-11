# Algoritmo g4_4
edades = []

suma = 0
edad_minima = float('inf')  # Un valor alto para iniciar la comparación

for i in range(20):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    edades.append(edad)
    suma += edad

    if edad < edad_minima:
        edad_minima = edad

promedio = suma / 20
print("El promedio de edad es:", promedio)
print("La edad de la persona más joven es:", edad_minima)
