import Pilas
from os import system

def menu():
    print('1. Push')
    print('2. Pop')
    print('3. Libera')
    print('4. Salir')
    return input('Cuál es tu opción? ')    

def casos(opcion, P):
    match opcion:
        case '1':
            x = input('Teclea dato a insertar ')
            P.push(x)
        case '2':
            if not P.estaVacia():
                print(f'Sale {P.pop()}')
            else:
                print('La pila está vacía...')
            system('pause')
        case '3':
            P.liberaMemoria()
            system('pause')
        case '4':
            print('Adiós!')
        case _:
            print('Opción inválida!')
            system('pause')

if __name__ == '__main__':
    system('cls')
    P = Pilas.Pila()
    
    opcion = None
    while opcion!='4':
        system('cls')
        opcion = menu()
        casos(opcion, P)
