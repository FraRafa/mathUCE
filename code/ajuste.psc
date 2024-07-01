Algoritmo Ajuste
	definir x,w,z Como real
	definir R Como real
	escribir "el valor del porcentaje x"
	leer x
	escribir "el valor del porcentaje w"
	leer w
	escribir "el valor del porcentaje z"
	leer z
	R<-((0.08 * x / (0.004 * w)) + (1.5 * z)) ^ 0.2
	escribir "El resultado de la operacion:", R
FinAlgoritmo
