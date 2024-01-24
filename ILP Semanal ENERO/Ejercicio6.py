# 6.Pedir un número y decir si es par o impar.

#ENTRADA DE DATOS

numero = int(input("Por favor, ingresa un número: "))

#PROCESOS
# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")