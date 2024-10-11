Algoritmo g3_7
	Definir tenis, futbol, n Como Entero
	Definir totalEdadTenis, totalEdadFutbol Como Entero
	tenis <- 0
	futbol <- 0
	totalEdadTenis <- 0
	totalEdadFutbol <- 0
	Escribir 'numero de socios'
	Leer n
	Definir numSocio, edad, deporte Como Entero
	Para i<-1 Hasta n Hacer
		Escribir 'Ingrese el número de socio'
		Leer numSocio
		Escribir 'Ingrese la edad'
		Leer edad
		Escribir 'Ingrese el deporte: 1-Tenis, 2-Rugby, 3-Voley, 4-Hockey, 5-Futbol'
		Leer deporte
		Si (deporte)=(1) Entonces
			tenis <- tenis+1
			totalEdadTenis <- totalEdadTenis+edad
		SiNo
			Si (deporte)=(5) Entonces
				futbol <- futbol+1
				totalEdadFutbol <- totalEdadFutbol+edad
			FinSi
		FinSi
	FinPara
	Escribir 'Cantidad de socios que practican tenis: ', tenis
	Escribir 'Cantidad de socios que practican fútbol: ', futbol
	Si tenis>0 Entonces
		Escribir 'Promedio de edad de jugadores de tenis: ', totalEdadTenis/tenis
	FinSi
	Si futbol>0 Entonces
		Escribir 'Promedio de edad de jugadores de fútbol: ', totalEdadFutbol/futbol
	FinSi
FinAlgoritmo
