#9.- realizar un Menú de Opciones y realizar una función para cada opción
# a) Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación
# b) Calcular la nómina de un empleado en ENERO del 2024
# c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
# d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos
import random

#DECLARAR O CREAR UNA FUNCION

def Pasaje():
    print("ADO:****")
    print("ALTAMAR:***")
    print("TAP:***")

def Nomina():
    mes = input("Ingrese el mes laborado:")
    dias_laborados = float(input("Ingrese el numero de dias que laboró:"))
    pago_dia = float(input("Ingrese el sueldo que se paga por día:"))

    pago_bruto = (pago_dia * dias_laborados)
    iva_tras = (pago_bruto * 0.16)
    sub_total = (pago_bruto + iva_tras)
    iva_rete = ((2/3) * iva_tras)
    isr_rete = (sub_total * 0.10)
    sueldo_neto = (sub_total - iva_rete - isr_rete)
    return  sueldo_neto

   

def generar_contrasena(longitud):
    caracteres = ["a", "b", "C", "D", "1", "8", "_", "*",]
    contraseña = ""
    for _ in range(longitud): 
        contraseña += caracteres[random.randint(0,7)]
    return contraseña

    # import secrets
    # import string

    # caracteres = string.ascii_letters + string.digits + string.punctuation
    # contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    # return contrasena

# Solicitar al usuario la longitud deseada para la contraseña
    

# Generar la contraseña

# Mostrar la contraseña generada
  
    
def Personal():
    apellido_1 = (input("Ingrese su apellido paterno: "))
    apellido_2 = (input("Ingrese su apellido materno: "))
    nombre = (input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))

    print(f"¡Que tal!, su nombre es {nombre} {apellido_1} {apellido_2} y tiene {edad} años.")


    #Mandar a llamar una funncion o invicarla para ejecutarla
print("***********MENÚ***********")
print("1. Servicios de pasaje")
print("2. Calculo de nómina")
print("3. Generar Contraseña")
print("4. Datos Personales")
opción = int(input("Ingrese una opción: "))


if(opción<1 or opción>4 ):
    print("Elija una opcion valida")

if(opción==1):
    Pasaje()

elif(opción==2): 
    print("Tu sueldo neto es: ", round(Nomina(), 2))

elif(opción==3):
    caracteres = int(input("Ingrese el número de caracteres de la contraseña: "))
    print("Contraseña = ", generar_contrasena(caracteres))

elif(opción==4):
    Personal()
