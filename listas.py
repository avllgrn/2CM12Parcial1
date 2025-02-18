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

def concatenaListas(l1, l2):
    l3 = []

    for dato in l1:
        l3.append(dato)

    for dato in l2:
        l3.append(dato)

    return l3

if __name__ == '__main__':
    system('cls')
    n = int(input('Dame n '))
    m = int(input('Dame m '))

    A = generaRand(n,-100,101)
    B = generaRand(m,-100,101)

    C = concatenaListas(A, B)

    print('\nA')
    muestraLista(A)
    print('\nB')
    muestraLista(B)
    print('\nC')
    muestraLista(C)
    