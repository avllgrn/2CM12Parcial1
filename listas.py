from os import system
from random import randrange
import Pilas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    Original = Pilas.Pila()

    for i in range(n):
        x = randrange(101)
        print(f'Original.push({x})')
        Original.push(x)
    print()


    Invertida = Pilas.Pila()

    while not Original.estaVacia():
        Invertida.push( Original.pop() )

    print('\nOriginal')
    Original.liberaMemoria()
    print('\nInvertida')
    Invertida.liberaMemoria()
    