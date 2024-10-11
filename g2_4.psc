Algoritmo g2_4
	Definir dni Como Cadena
	Definir categoria Como Entero
	Definir sueldbruto, descJ, descOS, descClub, sueldN Como Real
	Escribir 'Ingrese el DNI del empleado:'
	Leer dni
	Escribir 'Ingrese la categoría del empleado (0-Maestranza, 1-Administración, 2-Gerencia):'
	Leer categoria
	Según categoria Hacer
		0:
			sueldbruto <- 23600
			descJ <- sueldbruto*0.11
			descOS <- sueldbruto*0.03
			descClub <- 0
			nombreCat <- 'Maestranza'
		1:
			sueldbruto <- 35800
			descJ <- sueldbruto*0.11
			descOS <- sueldbruto*0.05
			descClub <- 0
			nombreCat <- 'Administración'
		2:
			sueldbruto <- 60420
			descJ <- sueldbruto*0.11
			descOS <- sueldbruto*0.05
			descClub <- sueldbruto*0.04
			nombreCat <- 'Gerencia'
		De Otro Modo:
			Escribir 'Categoría inválida'
	FinSegún
	sueldN <- sueldbruto-(descJ+descOS+descClub)
	Escribir 'DNI:', dni
	Escribir 'Categoría:', nombreCat
	Escribir 'Sueldo Neto:', sueldN
FinAlgoritmo
