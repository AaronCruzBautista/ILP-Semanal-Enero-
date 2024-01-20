#2. Calcular el área y perímetro de un círculo.


#IMPORTAR LIBRERIAS

#ENTRADA DE DATOS
PI = 3.1416
radio_circulo = float(input("Escribe el radio de tu circunferencia: "))

#PROCESOS
perimetro =  2 * PI * radio_circulo
area = PI * (radio_circulo ** 2)


#SALIDA DE DATOS
print("El perímetro de tu circunferencia es:", round(perimetro,2))
print("El area de tu circunferencia es:", round(area,2))

