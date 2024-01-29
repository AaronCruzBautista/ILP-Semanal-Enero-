# 12. Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos 
# insertados uno por uno y ordenados de forma ascendente.

def lista():
    numeros = []

    for _ in range(10):
        elemento = int(input("Ingrese un número: "))
        numeros.append(elemento)

        numeros.sort()

    print("Lista ordenada de forma ascendente:", numeros)

lista()
