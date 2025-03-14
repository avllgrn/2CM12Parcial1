from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    Original = Pilas.Pila()
    Cola =Colas.Cola()

    for i in range(n):
        x = randrange(101)
        print(f'Original.push({x})')
        Original.push(x)
    print()

    while not Original.estaVacia():
        Cola.push( Original.pop() )

    while not Cola.estaVacia():
        Original.push( Cola.pop() )

    print('\nOriginal')
    Original.liberaMemoria()
