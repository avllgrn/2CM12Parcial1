from os import system
from random import randrange
import Pilas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    Original = Pilas.Pila()
    Cola = Pilas.Pila()
    Auxiliar2 = Pilas.Pila()

    for i in range(n):
        x = randrange(101)
        print(f'Original.push({x})')
        Original.push(x)
    print()

    while not Original.estaVacia():
        Cola.push( Original.pop() )

    while not Cola.estaVacia():
        Auxiliar2.push( Cola.pop() )

    while not Auxiliar2.estaVacia():
        Original.push( Auxiliar2.pop() )

    print('\nOriginal')
    Original.liberaMemoria()
