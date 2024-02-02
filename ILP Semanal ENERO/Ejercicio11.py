# 11. Pedir números enteros en un ciclo mientras sean positivos y en caso de
# que un número sea negativo cerrar el ciclo y al final promediar los
# números positivos ingresados por el usuario.

numero = float(input("Ingrese un número: "))
suma = 0
conta = 0

while (numero >= 0):
        print("Es número positivo: ")
        suma = suma + numero
        conta += 1
        numero = float(input("Ingrese un número: "))

promedio = suma/conta
print("El promedio es: ", promedio)
