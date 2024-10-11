# Algoritmo g4_3
sueldos = []

for i in range(10):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i}: "))
    sueldos.append(sueldo)

max_sueldo = sueldos[0]

for i in range(1, 10):
    if sueldos[i] > max_sueldo:
        max_sueldo = sueldos[i]

print("El mayor sueldo es:", max_sueldo)