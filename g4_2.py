# Algoritmo g4_2
n = int(input("Ingrese la cantidad de notas: "))
notas = []

aprobados = 0
desaprobados = 0

for i in range(n):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)
