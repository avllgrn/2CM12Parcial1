import Pilas
from os import system

if __name__ == '__main__':
    system('cls')
    P = Pilas.Pila()
    decimal = int(input('Ingresa numero base diez '))
    
    x = decimal
    while x>0:
        P.push(x%2)
        x //= 2
        
    while not P.estaVacia():
        print(P.pop(), end='')
