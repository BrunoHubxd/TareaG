# Función que compara las edades
def comparar_edades(edad1, edad2):
    if edad1 > edad2:
        print(f"El hermano 1 es mayor por {edad1 - edad2} años.")
    elif edad2 > edad1:
        print(f"El hermano 2 es mayor por {edad2 - edad1} años.")
    else:
        print("Ambos hermanos tienen la misma edad.")

# Solicitar edades
edad1 = int(input("Ingrese la edad del hermano 1: "))
edad2 = int(input("Ingrese la edad del hermano 2: "))

# Llamada a la función
comparar_edades(edad1, edad2)
