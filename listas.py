from os import system
from random import randrange

def generaRand(tam, ini, fin):
    l = []

    for i in range(tam):
        l.append(randrange(ini, fin))

    return l

def muestraLista(l):
    tam = len(l)
    for i in range(tam):
        print(f'[{i}] = {l[i]}')





if __name__ == '__main__':
    system('cls')
    n = int(input('Dame n '))

    L = generaRand(n,0,11)
    print(f'L={L}, {type(L)}, tam {len(L)}')
    muestraLista(L)
    print()

    x = int(input('Cuál dato deseas borrar? '))
    if x in L:
        L.remove(x)
    print(f'L={L}, {type(L)}, tam {len(L)}')
    muestraLista(L)
    print()
