#2.	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta hacia atrás desde ese número hasta cero:

def par():
    numero = int(input("Introduzca un número par positivo: "))
    while numero < 0:
        numero = int(input("Introducir un número par positivo: "))
    for i in range(numero, -1, -1):
     print(i, end=" ")    
par()