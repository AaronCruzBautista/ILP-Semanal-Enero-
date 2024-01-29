#8. Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendo

#Entreda de datos 
mes = input("Ingrese el mes laborado:")
dias_laborados = float(input("Ingrese el numero de dias que laboró:"))
pago_dia = float(input("Ingrese el sueldo que se paga por día:"))

#PROCESOS
pago_bruto = (pago_dia * dias_laborados)
iva_tras = (pago_bruto * 0.16)
sub_total = (pago_bruto + iva_tras)
iva_rete = ((2/3) * iva_tras)
isr_rete = (sub_total * 0.10)
sueldo_neto = (sub_total - iva_rete - isr_rete)

print("Tu sueldo neto es: ", round(sueldo_neto,2))