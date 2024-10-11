Algoritmo g2_1
	Definir categoria Como Entero
	Definir sueldbruto, descJ, descOS, sueldN, bono Como Real
	Escribir 'Ingresa la categoría del empleado (1-repositor, 2-cajero, 3-supervisor)'
	Leer categoria
	Según categoria Hacer
		1:
			sueldbruto <- 32335
			bono <- sueldbruto*0.08
		2:
			sueldbruto <- 38630.89
			bono <- 0
		3:
			sueldbruto <- 45560.20
			bono <- 0
		De Otro Modo:
			Escribir 'Categoría inválida'
	FinSegún
	descJ <- sueldbruto*0.11
	descOS <- sueldbruto*0.03
	sueldN <- sueldbruto-(descJ+descOS)
	Escribir 'Sueldo Bruto: ', sueldbruto
	Escribir 'Descuento por Jubilación: ', descJ
	Escribir 'Descuento por Obra Social: ', descOS
	Escribir 'Sueldo Neto: ', sueldN
	Si bono>0 Entonces
		Escribir 'Bono en compras para repositores: ', bono
	FinSi
FinAlgoritmo
