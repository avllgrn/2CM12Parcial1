from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    lista1 = []
    lista2 = []
    conjunto1 = set()
    conjunto2 = set()
    
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        lista1.append(x)
        lista2.append(y)
        
    print(f'Lista1 = {lista1}')
    print(f'Lista2 = {lista2}')
    
    for i in range(len(lista1)):
        conjunto1.add(lista1[i])
        conjunto2.add(lista2[i])
        
    conjunto3 = conjunto1.union(conjunto2)
    conjunto4 = conjunto1.intersection(conjunto2)

    print(f'conjunto1 = {conjunto1}')
    print(f'conjunto2 = {conjunto2}')
    print(f'conjunto3 = {conjunto3}')
    print(f'conjunto4 = {conjunto4}')
