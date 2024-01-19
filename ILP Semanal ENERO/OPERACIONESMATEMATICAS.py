#Operaciones Matematicas (SUMA, RESTA, MULTIPLICACION, DIVISION, POTENCIA, RAIZ CUADRADA Y MODULO)
#IMPORTAR LIBRERIAS 
import math
#Entrada de datos
nombre_completo = "Aaron C.B."
edad = 20
numero1 = float(input("Ingresa un numero: "))
numero2 = float(input("Ingresa otro numero: "))
#PROCESOS(operaciones y/o calculos matematicos o logicos)
suma = numero1 + numero2
resta =  numero1 - numero2
MULTIPLICACION = numero1 * numero2
DIVISION = numero1/numero2

POTENCIA_1 = numero1 ** numero2 #10 elevado a la 5.7
POTENCIA_2 = pow(numero1,numero2)

cuadrado = numero1 ** 2
cubo = numero1 ** 3

raiz_cuadrada_1 = math.sqrt(27)
raiz_cuadrada_2 = pow(27, 1/2)
raiz_cubica = pow(27, 1/3)

modulo_residuo = numero1 % numero2

#SALIDA DE DATOS 
print(nombre_completo)
print(edad)
print("la suma es = ", suma)
print("la resta es = ", resta)
print("la multiplicacion es = ", MULTIPLICACION)
print("la division es = ", round(DIVISION,2))
print("la potencia es = ", POTENCIA_1)
print("la POTENCIA es = ", POTENCIA_2)
print("el cuadrado es = ", cuadrado)
print("cubo es = ", cubo)
print("la raiz es = ", raiz_cuadrada_1)
print("la raiz es = ", raiz_cuadrada_2)
print("la raiz cubica es = ", raiz_cubica)
print("el residuo es = ", modulo_residuo)