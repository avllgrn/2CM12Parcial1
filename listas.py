from os import system
from random import randrange
import Pilas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    Original = Pilas.Pila()
    Copia = Pilas.Pila()
    Auxiliar = Pilas.Pila()

    for i in range(n):
        x = randrange(101)
        print(f'Original.push({x})')
        Original.push(x)
    print()

    while not Original.estaVacia():
        Auxiliar.push( Original.pop() )

    while not Auxiliar.estaVacia():
        temp =Auxiliar.pop()
        Original.push( temp )
        Copia.push( temp )

    print('\nOriginal')
    Original.liberaMemoria()
    print('\nCopia')
    Copia.liberaMemoria()
