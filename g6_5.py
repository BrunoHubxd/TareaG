# Función que ordena dos números de menor a mayor
def ordenar(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    
    print("Los números ordenados de menor a mayor son:", menor, "y", mayor)

# Solicitar los números al usuario
a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))

# Llamar a la función para ordenar
ordenar(a, b)
