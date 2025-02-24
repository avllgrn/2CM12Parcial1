from os import system
from random import randrange

def generaListaRand(tam, ini, fin):
    l = []

    for i in range(tam):
        l.append(randrange(ini, fin))

    return l

def muestraContenedor(l):
    tam = len(l)
    for i in range(tam):
        print(f'[{i}] = {l[i]}')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos necesitas? '))

    lista = generaListaRand(n, 0, 101)  #Se genera lista con valores aleatorios
    tupla = tuple(lista)                #Se genera tupla con valores de lista

    print(f'lista{lista}, {type(lista)}, tam {len(lista)}')
    muestraContenedor(lista)
    print()

    print(f'tupla{tupla}, {type(tupla)}, tam {len(tupla)}')
    muestraContenedor(tupla)
    print()
