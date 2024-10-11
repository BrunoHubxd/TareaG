# Función que verifica si el alumno está aprobado
def esta_aprobado(nota1, nota2, nota3):
    if nota1 > 4 and nota2 > 4 and nota3 > 4:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            return True
        else:
            return False
    else:
        return False

# Solicitar las notas del alumno
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Verificar si está aprobado
if esta_aprobado(nota1, nota2, nota3):
    print("El alumno está aprobado.")
else:
    print("El alumno no está aprobado.")
