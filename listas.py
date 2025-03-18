from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    conjunto1 = set()
    conjunto2 = set()
    lista1 = []
    lista2 = []
    diccionario = {}
        
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        conjunto1.add(x)
        conjunto2.add(y)

    print(f'conjunto1 = {conjunto1}')
    print(f'conjunto2 = {conjunto2}')

    if len(conjunto1) == len(conjunto2):
        for i in conjunto1:
            lista1.append(i)

        for i in conjunto2:
            lista2.append(i)
            
        for i in range(len(lista1)):
            diccionario.update( { lista1[i] : lista2[i]} )

    print(f'diccionario = {diccionario}')
