#Calcular el salario
print("Calculadora de salario")
print("Ingrese el nombre del empleado:")
nombre=input()
print("Ingrese el salario base del empleado:")
sal_base=float(input())
print("Ingrese el número de horas extras trabajadas")
num_horas=float(input())
sbu=460
horas_extras=num_horas*(sal_base/160)
fondos_reserva=(sal_base+horas_extras)*0.0833
d_tercero=(sal_base+horas_extras)/12
d_cuarto=(sbu/12)
vac=(sal_base)/24
IESS_trab=(sal_base+horas_extras)*0.0945
IESS_empl=(sal_base+horas_extras)*0.1215
total_ingresos=sal_base+horas_extras+fondos_reserva
total_descuentos=IESS_trab
sal_final=total_ingresos-total_descuentos
print("ROL DE PAGOS DE ",nombre)
print("INGRESOS:")
print("Salario base: ",sal_base," USD")
print("Horas extras: ",horas_extras," USD")
print("Fondos de Reserva 8,33%: ",fondos_reserva," USD")
print("Total INGRESOS: ",total_ingresos, "USD")
print("DESCUENTOS:")
print("Aporte IESS empleado 9,45%: ",IESS_trab," USD")
print("Total DESCUENTOS: ",total_descuentos)
print("TOTAL SUELDO NETO A RECIBIR: ",sal_final," USD")
print("Detalle de beneficios sociales del mes:")
print("Décimo tercer sueldo: ",d_tercero," USD")
print("Décimo cuarto sueldo: ",d_cuarto," USD")
print("Vacaciones: ",vac," USD")
print("Detalle de otros costos relacionados:")
print("Aporte IESS Empleador 12,15%: ",IESS_empl," USD")