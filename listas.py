from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    Conjunto = set()

    while len(Conjunto)<10:
        Conjunto.add(randrange(101))
    
    print(Conjunto, type(Conjunto), len(Conjunto))

    x = int(input('Cuál quieres eliminar? '))
    if x in Conjunto:
        Conjunto.remove(x)
    print(Conjunto, type(Conjunto), len(Conjunto),'\n')

    x = int(input('Cuál quieres eliminar? '))
    Conjunto.discard(x)
    print(Conjunto, type(Conjunto), len(Conjunto),'\n')

    x = Conjunto.pop()
    print(f'Sale {x}', end=' ')
    Conjunto.discard(x)
    print(Conjunto, type(Conjunto), len(Conjunto),'\n')
