#1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#IMPORTAR LIBRERIAS

#ENTRADA DE DATOS
#DECLARAR, CREAR O INSTANCIAR VARIABLES
calificacion_1 = float(input("Ingresa la primera calificacion: "))
calificacion_2 = float(input("Ingresa la segunda calificacion: "))
calificacion_3 = float(input("Ingresa la tercera calificacion: "))


#PROCESOS
#JERARQUIA DE OPERADORES
#1 POTENCIA Y RAIZ
#2 MULTI Y DIVI
#3 SUMA Y RESTA
promedio = (calificacion_1 + calificacion_2 + calificacion_3)/3
print("El promedio de las 3 calificaciones es:", round(promedio,2))
if (promedio>6 and promedio<=10):
    print("APROBADO")
elif(promedio == 6):
    print("APENAS APROBADO")
elif(promedio>=0 and promedio < 6):
    print("REPROBADO")
elif(promedio<0 or promedio>10):
    print("PROMEDIO NO VALIDO")
#CAMBIOS



