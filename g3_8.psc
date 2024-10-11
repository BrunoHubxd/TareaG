Algoritmo g3_8
	Definir doc, edad, sexo Como Entero
	Definir cantTotal, cantHombres, cantMujeres, cantHombresJovenes Como Entero
	Definir maxEdad, docMayorEdad Como Entero
	cantTotal <- 0
	cantHombres <- 0
	cantMujeres <- 0
	cantHombresJovenes <- 0
	maxEdad <- -1
	docMayorEdad <- 0
	Escribir 'Ingrese el número de documento (0 para finalizar)'
	Leer doc
	Mientras doc<>0 Hacer
		cantTotal <- cantTotal+1
		Escribir 'Ingrese la edad'
		Leer edad
		Escribir 'Ingrese el sexo (1 para masculino, 2 para femenino)'
		Leer sexo
		Si sexo=1 Entonces
			cantHombres <- cantHombres+1
			Si edad>=16 Y edad<=65 Entonces
				cantHombresJovenes <- cantHombresJovenes+1
			FinSi
		SiNo
			cantMujeres <- cantMujeres+1
		FinSi
		Si edad>maxEdad Entonces
			maxEdad <- edad
			docMayorEdad <- doc
		FinSi
		Escribir 'Ingrese el número de documento (0 para finalizar)'
		Leer doc
	FinMientras
	Escribir 'Cantidad total de personas censadas: ', cantTotal
	Escribir 'Cantidad de hombres censados: ', cantHombres
	Escribir 'Cantidad de mujeres censadas: ', cantMujeres
	Si cantHombres>0 Entonces
		Escribir 'Porcentaje de hombres entre 16 y 65 años: ', (cantHombresJovenes*100)/cantHombres
	FinSi
	Escribir 'Mayor edad registrada: ', maxEdad, ' con número de documento: ', docMayorEdad
FinAlgoritmo
