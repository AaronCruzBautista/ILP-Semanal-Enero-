#Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, 
# muestre su resultado aciertos / 12 y mostrar el calificación = (aciertos / 12) * 10
aciertos = 0
print("*****CUESTIONARIO*****")
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código. a) IDE  b) Pseudocódigo  c) Compilador  d) ANSI / ISO")
respuesta = input("Ingresa tu respuesta: ")
if (respuesta == "b"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados. a) Información  b) Datos  c) Programa  d) Código")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "b"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados. a) Información  b) Datos  c) Programa  d) Código")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "c"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo. a) IEEE  b) IDE  c) ANSI/ISO  d) VSCode")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "c"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema. a) Proceso  b) Solución  c) Función  d) Algoritmo")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "d"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("5. Conjunto de elementos que se relacionan para cumplir una función determinada. a) Estructura  b) Datos  c) Operación  d) Sistema")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "c"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina. a) Depurador  b) Editor de Texto  c) Terminal de Salida  d) Compilador/Intérprete")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "d"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor. a) Constante  b) Variable  c) Librería  d) Tipo de Dato")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "b"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("8. Conjunto de símbolos, letras, números que no tienen un significado. a) Datos  b) Estructura  c) Información  d) Sistema")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "a"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento. a) Filosofía  b) Sociología  c) Lógica  d) Argumentación")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "c"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto. a) Evento  b) Estándar  c) Calidad  d) Productividad")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "b"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico. a) Estructura  b) Sistema  c) Objeto  d) Virtual")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "b"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar. a) Operaciones/Cálculos  b) Sintaxis  c) Programa de Computadora  d) Comando")
respuesta = input("Ingresa tu respuesta: ")
if(respuesta == "c"):
    print("correcto")
    aciertos += 1
else:
    print("Incorrecto")

promedio = (aciertos/12) * 10
print("Obtuviste:", aciertos, "de 12." "Tu promedio es:", promedio)

