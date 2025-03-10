from os import system
import Pilas
import Colas

def esCapicua(numero):
    P = Pilas.Pila()
    C = Colas.Cola()

    for digito in numero:
        P.push(digito)
        C.push(digito)

    while not C.estaVacia() and not P.estaVacia():
        if P.pop() != C.pop():
            return False
    return True

if __name__ == '__main__':
    system('cls')
    
    numero = input('Ingresa numero ')
    
    if esCapicua(numero):
        print(f'{numero} ES capicúa =)')
    else:
        system('cls')
        print(f'{numero} NO es capicúa =(')
