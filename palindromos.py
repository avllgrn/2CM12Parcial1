from os import system
import Pilas
import Colas

def esPalindromo(cadena):   #INCOMPLETO
    P = Pilas.Pila()
    C = Colas.Cola()

    for caracter in cadena:
        if caracter.isalnum():
            P.push(caracter.lower())
            C.push(caracter.lower())

    while not C.estaVacia() and not P.estaVacia():
        if P.pop() != C.pop():
            print()
            return False
    return True

if __name__ == '__main__':
    system('cls')
    
    cadena = input('Ingresa cadena ')
    
    if esPalindromo(cadena):
        print(f'{cadena} ES palíndromo =)')
    else:
        system('cls')
        print(f'{cadena} NO es palíndromo =(')
