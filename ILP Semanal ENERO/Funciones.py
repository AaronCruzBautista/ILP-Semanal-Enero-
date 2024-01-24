#FUNCIONES.- Son tareas a ejecutar o realizar
#SINTAXIS

# def Nombre_de_funcion(parametro o argumentos):
#     instrucciones o procesos que va arealizar la funcion 
#     return valor    (Se dice que devuelve, retorna o regresa un valor)

#DECLARAR O CREAR UNA FUNCION

def Saludar():
    print("Hola Mundo")

def Sumar(num1, num2):
    suma = num1 + num2
    return suma

def Restar(num1, num2):
    return num1 - num2

def Multiplicar(num1, num2):
    return num1 * num2

def División(num1, num2):
    return num1/num2

#Mandar a llamar una funncion o invicarla para ejecutarla
print("***********MENÚ***********")
print("1. Saludo")
print("2. Suma")
print("3. Resta")
print("4. Multiplicación")
print("5. División")
opción = int(input("Ingrese una opción: "))



if(opción==1):
    Saludar()

elif(opción==2):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print("La suma de los dos datos es:", Sumar(num1, num2))
elif(opción==3):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print("La resta de los dos datos es:", Restar(num1, num2))

elif(opción==4):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print("La Multiplicación de los dos datos es:", Multiplicar(num1, num2))

elif(opción==5):
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print("La División de los dos datos es:", División(num1, num2))

else:
    print("Opción no valida")


