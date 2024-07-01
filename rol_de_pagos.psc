Algoritmo sin_titulo
	Definir sal_base, sbu, num_hora, horas_extras, fondo_reserva, d_tercero, d_cuarto, vac, iess_trab, iess_empl, total_ingresos, total_descuentos, sal_final Como Real
	Definir nombre Como Caracter
	sbu <- 460
	
	Escribir "CALCULADORA DE SALARIO"
	Escribir "Ingrese el nombre del empleado:"
	Leer nombre
	
	Escribir "Ingrese el salario base del empleado:"
	Leer sal_base
	
	Escribir "Ingrese el número de horas extras trabajadas"
	Leer num_hora
	
	horas_extras <- num_hora*(sal_base/160)
	fondo_reserva <- (sal_base+horas_extras)*0.0833
	d_tercero <- (sal_base+horas_extras)/12
	d_cuarto <- sbu/12
	vac <- sal_base/24
	iess_trab <- (sal_base+horas_extras)*0.0945
	iess_empl <- (sal_base+horas_extras)*0.1215
	total_ingresos <- sal_base+horas_extras+fondo_reserva
	total_descuentos <- iess_trab
	sal_final <- total_ingresos-total_descuentos
	
	Escribir "ROL DE PAGOS DE:", nombre
	Escribir "INGRESOS:"
	Escribir "Salario base:", sal_base, " USD"
	Escribir "Horas extras:", horas_extras, " USD"
	Escribir "Fondos de reserva 8,33%:", fondo_reserva, " USD"
	Escribir "TOTAL INGRESOS:", total_ingresos, " USD"
	Escribir "DESCUENTOS:"
	Escribir "Aporte IESS empleado:", iess_trab, " USD"
	Escribir "TOTAL DESCUETOS:", total_descuentos, " USD"
	Escribir "TOTAL SUELDO NETO A RECIBIR:", sal_final, " USD"
	Escribir "DETALLE BENEFICIOS SOCIALES:"
	Escribir "Décimo tercer sueldo:", d_tercero, " USD"
	Escribir "Décimo cuarto sueldo:", d_cuarto, " USD"
	Escribir "Vacaciones:", vac, " USD"
	Escribir "Detalle de otros costos relacionados:"
	Escribir "Aporte IESS empleador:", iess_empl, " USD"
	
	
	
FinAlgoritmo
