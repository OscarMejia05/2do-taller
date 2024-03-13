# 1.Crea un programa que usando bucles nos permita pedir un número par comprendido entre 100 y 200 y nos muestre todos los números pares comprendidos entre el número ingresado y 200. Por ejemplo, si el número ingresado es 192 nos debería mostrar 192, 194, 196, 198 y 200.

def par():
    numero = int(input("Introduzca un número par entre 100 y 200: "))
    while numero % 2 != 0 or numero < 100 or numero > 200:
        numero = int(input("Número no valido, digite un número par entre 100 y 200: "))
    for i in range(numero, 201, 2):
     print(i)
    print()
par()