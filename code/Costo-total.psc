	Algoritmo CalculoBaldosas
		// Solicitar el ancho en metros
		Escribir "Ingrese el ancho en metros"
		Leer ancho		
		
		// Solicitar el largo en metros
		Escribir "Ingrese el largo en metros"
		Leer largo
		
		// Calcular el �rea
		area <- largo * ancho
		
		// Calcular el n�mero de baldosas necesarias
		numero_baldosas <- area / 0.003
		
		// Calcular el costo total
		costo_total <- numero_baldosas * 3.5
		
		// Mostrar los resultados
		Escribir "El �rea es:", area, "metros cuadrados"
		Escribir "El n�mero de baldosas a utilizar es:", numero_baldosas
		Escribir "El costo total es:", costo_total, "USD"
		Escribir "Gracias por usar nuestro programa."
FinAlgoritmo
