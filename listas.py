from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    diccionario = {}
    P = Pilas.Pila()
    C = Colas.Cola()
    
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        diccionario.update({ x:y })

    print(f'diccionario = {diccionario}')
    
    for i in diccionario:
        P.push(i)
        C.push(diccionario.get(i))

    print(f'Pila')
    P.liberaMemoria()
    print()

    print(f'Cola')
    C.liberaMemoria()
    print()
