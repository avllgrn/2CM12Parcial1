from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    diccionario = {}
    conjunto1 = set()
    conjunto2 = set()
    
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        diccionario.update({ x:y })

    print(f'diccionario = {diccionario}')
    
    for i in diccionario:
        conjunto1.add(i)
        conjunto2.add(diccionario.get(i))

    conjunto3 = conjunto1.union(conjunto2)
    conjunto4 = conjunto1.intersection(conjunto2)

    print(f'conjunto1 = {conjunto1}')
    print(f'conjunto2 = {conjunto2}')
    print(f'conjunto3 = {conjunto3}')
    print(f'conjunto4 = {conjunto4}')
