from os import system
from random import randrange

def funcionConInput():
    V = []
    n = int(input('Cuantos datos? '))

    for i in range(n):
        dato = float(input(f'Ingresa [{i}] '))
        print(dato, type(dato))
        V.append(dato)

    print(V)

def funcionConRandrange():
    V = []
    n = int(input('Cuantos datos? '))

    for i in range(n):
        dato = randrange(50, 60)
        print(dato, type(dato))
        V.append(dato)

    print(V)

if __name__ == '__main__':
    system('cls')
    funcionConInput()
    print()
    funcionConRandrange()
    print()