# Función que determina el tipo de triángulo
def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        return "Escaleno"
    else:
        return "Isósceles"

# Solicitar los lados del triángulo
lado1 = float(input("Ingrese el lado 1 del triángulo: "))
lado2 = float(input("Ingrese el lado 2 del triángulo: "))
lado3 = float(input("Ingrese el lado 3 del triángulo: "))

# Determinar y mostrar el tipo de triángulo
tipo = tipo_triangulo(lado1, lado2, lado3)
print("El tipo de triángulo es:", tipo)
