from os import system
from random import randrange

def generaRand(tam, ini, fin):
    l = []

    i = 0
    while i < tam:
        l.append(randrange(ini, fin))
        i += 1

    return l

def muestraLista(l):
    tam = len(l)
    
    i = 0
    while i < tam:
        print(f'[{i}] = {l[i]}')
        i += 1

def concatenaListas(l1, l2):
    l3 = []
    
    tam = len(l1)    
    i = 0
    while i < tam:
        l3.append(l1[i])
        i += 1

    tam = len(l2)
    i = 0
    while i < tam:
        l3.append(l2[i])
        i += 1

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
    