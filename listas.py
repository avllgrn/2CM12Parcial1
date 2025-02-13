from os import system
from random import randrange

def funcionConRandrange():
    V = []
    n = int(input('Cuantos datos? '))

    for i in range(n):
        dato = randrange(100)
        print(dato, type(dato))
        V.append(dato)
    print(V)

    posicion = int(input('Cual quieres cambiar? '))
    V[posicion] = -123
    print(V)


if __name__ == '__main__':
    system('cls')
    funcionConRandrange()
    print()