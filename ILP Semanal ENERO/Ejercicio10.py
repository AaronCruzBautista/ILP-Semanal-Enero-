# 10. Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido
num = int(input("Ingresa tu valor:"))

if(num < 0 and num > -100):
    for i in range(-1, -101, -2):
        print("", i)
elif(num == 0 or num <= -100 or num >= 100):
    print("NO VALIDO")
if(num > 0 and num < 100):
    j = 0
    while(j <= 100):
        print("", j)
        j = j + 2
