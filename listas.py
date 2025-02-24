from os import system
from random import randrange

def funcion(*argumentos):
    print(f'argumentos = {argumentos} tamaño = {len(argumentos)} type = {type(argumentos)}')
    print('Contenido de argumentos:')
    for dato in argumentos:
        print(f'{dato} type = {type(dato)}')
    print()

if __name__ == '__main__':
    system('cls')

    funcion()
    funcion(1)
    funcion(2.3)
    funcion('cuatro')
    funcion(5, 6, 7, 8)
    funcion(9.8, 7.6, 5.4, 3.2, 1.0)
    funcion('uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis' )
