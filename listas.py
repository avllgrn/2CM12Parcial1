import Colas
from os import system
from random import randrange


def menu():
    print('1. Push')
    print('2. Pop')
    print('3. Libera')
    print('4. Salir')
    return input('Cuál es tu opción? ')    

def casos(opcion, C):
    match opcion:
        case '1':
            x = input('Teclea dato a insertar ')
            C.push(x)
        case '2':
            if not C.estaVacia():
                print(f'Sale {C.pop()}')
            else:
                print('La cola está vacía...')
            system('pause')
        case '3':
            C.liberaMemoria()
            system('pause')
        case '4':
            print('Adiós!')
        case _:
            print('Opción inválida!')
            system('pause')

if __name__ == '__main__':
    system('cls')
    C = Colas.Cola()
    
    opcion = None
    while opcion!='4':
        system('cls')
        opcion = menu()
        casos(opcion, C)
