
#DECLARAR O CREAR UNA LISTA
edades = [20, 30, 40, 50]
nombres = ["Michelle", "Hugo", "Aaron", "Ignacio"]
#indice      0            1       2            3 index


#operaciones con arreglos/listas
#agregar o insertar un elemento al final de la lista
nombres.append("Eduardo")
edades.append(60)

#Eliminar un elemento de una lista
nombres.remove("Hugo")
edades.remove(30)

#Acceder y editar a un elemento de una lista
nombres[0] = "Miguel"
edades[0] = 25

#obtener la longitud de una lista
print(len(nombres)) #lenght
print(len(edades))

# ordenar una lista
nombres.sort()
edades.sort(reverse=True)

print("NOMBRE:", nombres)
print("EDADES:", edades)