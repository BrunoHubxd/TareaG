Algoritmo g3_5
	Definir dni, tipoServ Como Entero
	Definir monto Como Real
	Para i<-1 Hasta 5 Hacer
		Escribir 'Ingrese el DNI del cliente'
		Leer dni
		Escribir 'Ingrese el tipo de servicio: 1-30M, 2-50M, 3-100M'
		Leer tipoServ
		Si (tipoServ)=(1) Entonces
			monto <- 750
		SiNo
			Si (tipoServ)=(2) Entonces
				monto <- 1100
			SiNo
				monto <- 1500*0.95
			FinSi
		FinSi
		Escribir 'DNI: ', dni
		Escribir 'Monto a pagar: ', monto
		Escribir 'Tipo de servicio: ', tipoServ
	FinPara
FinAlgoritmo
