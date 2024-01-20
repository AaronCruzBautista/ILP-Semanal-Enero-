#4. Pedir la cantidad de grados y convertirlos a °C, °F y K.


#IMPORTAR LIBRERIAS

#ENTRADA DE DATOS
cel = float (input("Escribe los grados en celcius: "))
fhar = float (input("Escribe los grados fharenheit: "))
kel = float (input("Escribe los grados kelvin: "))

#PROCESOS
celcius_1 = kel - 273.15
celcius_2 = (5*(fhar-32))/9
kelvin_1 = cel + 273.15
kelvin_2 = (5*(fhar-32))/ 9 + (273.15)
fhar_1 = (9*(kel-273.15))/ 5 + (32)
fhar_2 = (9*(cel))/5 +(32)
#SALIDA DE DATOS
print("La convercion de kelvin a celcius es:", round(celcius_1,2))
print("La convercion de fharenheit a celcius es:", round(celcius_2,2))
print("La convercion de celcius a kelvin es:", round(kelvin_1,2))
print("La convercion de fharenheit a kelvin es:", round(kelvin_2,2))
print("La convercion de kelvin a Fharenheit es:", round(fhar_1,2))
print("La convercion de celcius a Fharenheit es:", round(fhar_2,2))



