from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    P = Pilas.Pila()
    C = Colas.Cola()
    diccionario = {}
        
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        P.push(x)
        C.push(y)

    while not P.estaVacia() and not C.estaVacia():
        diccionario.update( { P.pop() : C.pop()} )

    print(f'diccionario = {diccionario}')

    print('Pila')
    P.liberaMemoria()
    print('Cola')
    C.liberaMemoria()
