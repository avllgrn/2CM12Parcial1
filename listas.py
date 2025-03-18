from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    P = Pilas.Pila()
    C = Colas.Cola()
    conjunto1 = set()
    conjunto2 = set()
        
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        P.push(x)
        C.push(y)

    while not P.estaVacia() and not C.estaVacia():
        conjunto1.add( P.pop() )
        conjunto2.add( C.pop() )

    print(f'conjunto1 = {conjunto1}')
    print(f'conjunto2 = {conjunto2}')

    print('Pila')
    P.liberaMemoria()
    print('Cola')
    C.liberaMemoria()
