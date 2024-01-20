#3. Determinar la edad de una persona conociendo el año actual y el año de nacimiento.
#IMPORTAR LIBRERIAS

#ENTRADA DE DATOS
actual = int (input("Escribe el año actual: "))
nacimiento = int (input("Escribe el año de tu nacimiento: "))
#PROCESOS
edad = actual - nacimiento

#SALIDA DE DATOS
print("Tu edad es de:", edad)
