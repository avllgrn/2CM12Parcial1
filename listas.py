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

    tam1 = len(l1)
    for i in range(tam1):
        l3.append(l1[i])

    tam2 = len(l2)
    for i in range(tam2):
        l3.append(l2[i])

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
    