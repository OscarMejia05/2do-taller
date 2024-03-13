#3.	Escribir un programa que muestre la siguiente serie de números basado en un número dado por el usuario

def numeropos():
    numero = int(input("Introduce un número positivo: "))
    while numero < 0:
        numero = int(input("Introduce un número positivo: "))
    for i in range(1, numero + 1):
        print(str(i) * i)
numeropos()