Algoritmo g3_6
	Definir mejorTiempo Como Real
	Definir vehiculo, tiempo Como Entero
	Definir mejorVehiculo Como Entero
	Para i<-1 Hasta 12 Hacer
		Escribir 'Ingrese el número del vehículo'
		Leer vehiculo
		Escribir 'Ingrese el tiempo (en segundos)'
		Leer tiempo
		Si (i)=(1) Entonces
			mejorTiempo <- tiempo
			mejorVehiculo <- vehiculo
		SiNo
			Si tiempo<mejorTiempo Entonces
				mejorTiempo <- tiempo
				mejorVehiculo <- vehiculo
			FinSi
		FinSi
	FinPara
	Escribir 'Mejor tiempo: ', mejorTiempo
	Escribir 'Número de vehículo: ', mejorVehiculo
FinAlgoritmo
