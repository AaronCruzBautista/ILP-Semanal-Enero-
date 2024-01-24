#7. Pedir el nivel del agua en metros de una cisterna

#ENTRADA DE DATOS
nivel = float(input("Dame el nivel de agua de la cisterna en metros:"))

#PROCESOS
if(nivel > 6):
    print("Desbordamiento de agua de cisterna")
elif(nivel == 6):
    print("Apagar bomba")
elif(nivel>4 and nivel<6):
    print("Desacelerar bomba")
elif(nivel>2 and nivel<=4):
    print("Bomba trabajando")
elif(nivel>0 and nivel<=2):
    print("Acelerar bomba de agua")
elif(nivel==0):
    print("Encender bomba de agua")
elif(nivel<0):
    print("Fuga en cisterna")
