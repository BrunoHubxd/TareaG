Algoritmo g2_2
	Definir cantidad Como Entero
	Escribir 'Ingrese la cantidad de paquetes:'
	Leer cantidad
	Si cantidad<5 Entonces
		Escribir 'No se permiten compras inferiores a 5 productos.'
	SiNo
		Si cantidad>=5 Y cantidad<=15 Entonces
			Escribir 'El costo de env�o es de $200.'
		SiNo
			Escribir 'El env�o es gratuito.'
		FinSi
	FinSi
FinAlgoritmo
