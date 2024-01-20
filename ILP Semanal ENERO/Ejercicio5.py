#5. Obtener valores para: a, b y c. Calcular la fórmula general.


#IMPORTAR LIBRERIAS
import math
#ENTRADA DE DATOS
datoa = float (input("Escribe el valor del dato a: "))
datob = float (input("Escribe el valor del dato b: "))
datoc = float (input("Escribe el valor del dato c: "))

#PROCESOS
x1 = (-datob-math.sqrt((datob **2)-4*datoa*datoc ))/(2*datoa)
x2 = (-datob+math.sqrt((datob **2)-4*datoa*datoc ))/(2*datoa)
#SALIDA DE DATOS
print("Tu resultado x1 es:", x1)
print("Tu resultado x2 es:", x2)

