from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    lista1 = []
    lista2 = []
    diccionario = {}
    
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        lista1.append(x)
        lista2.append(y)
        
    print(f'Lista1 = {lista1}')
    print(f'Lista2 = {lista2}')
    
    for i in range(len(lista1)):
        diccionario.update({lista1[i] : lista2[i]})
        
    print(f'diccionario = {diccionario}')
