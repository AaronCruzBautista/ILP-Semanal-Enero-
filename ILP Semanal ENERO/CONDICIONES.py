#MAYOR O MENOR DE EDAD


#ENTRADA DE DATOS
#DECLARAD O CREAR VARIABLES
edad =int(input("Ingresa tu edad:"))

#PROCESOS 
if(edad>=18 and edad>=120):   #Rango aceptado(18-120)
    print("Es mayor de edad")
elif(edad >= 0 and edad<18):      #rango aceptado(0 - <18)
    print("es menor de edad")
elif (edad < 0 or edad >120):                  #valores invalidos (<0 ,>120)
    print("edad no valida")
