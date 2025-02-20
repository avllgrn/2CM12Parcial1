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

def acumulaListas(l1, l2):
    s = 0
    for dato in l1:
        #print(s, dato)
        s += dato
    
    for dato in l2:
        #print(s, dato)
        s += dato

    return s

def sumaVectores(V1, V2):
    V3 = []

    if len(A)==len(B):
        for i in range(n):
            V3.append(V1[i]+V2[i])

    return V3

def restaVectores(V1, V2):
    V3 = []

    if len(A)==len(B):
        for i in range(n):
            V3.append(V1[i]-V2[i])

    return V3

if __name__ == '__main__':
    system('cls')
    n = int(input('Dame n '))
    m = int(input('Dame m '))

    A = generaRand(n,-100,11)
    B = generaRand(m,-100,11)

    print('\nA')
    muestraLista(A)
    print('\nB')
    muestraLista(B)
    
    C=sumaVectores(A,B)
    D=restaVectores(A,B)

    print('\nC')
    muestraLista(C)
    print('\nD')
    muestraLista(D)
