from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    P = Pilas.Pila()
    C = Colas.Cola()
    lista1 = []
    lista2 = []
        
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        P.push(x)
        C.push(y)

    while not P.estaVacia():
        lista1.append(P.pop())

    while not C.estaVacia():
        lista2.append(C.pop())
        
    print(f'lista1 = {lista1}')
    print(f'lista2 = {lista2}')

    print('Pila')
    P.liberaMemoria()
    print('Cola')
    C.liberaMemoria()
