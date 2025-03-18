from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    diccionario = {}
    lista1 = []
    lista2 = []
    
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        diccionario.update({ x:y })

    print(f'diccionario = {diccionario}')
    
    for i in diccionario:
        lista1.append(i)
        lista2.append(diccionario.get(i))
        
    print(f'Lista1 = {lista1}')
    print(f'Lista2 = {lista2}')
