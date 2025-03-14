from os import system
import Pilas

def verificaParentesis(expresion):
    P = Pilas.Pila()

    parejas = { '(':')' }

    for parentesis in expresion:
        if parentesis in parejas:
            P.push( parejas.get(parentesis) )
        elif parentesis in parejas.values() and P.estaVacia():
            return False
        elif parentesis in parejas.values() and not P.estaVacia():
            P.pop()

    if P.estaVacia():
        return True
    else:
        return False

if __name__ == '__main__':
    system('cls')
    
    expresion = input('Ingresa expresión ')
    
    if verificaParentesis(expresion):
        print(f'{expresion} ESTÁ balanceada =)')
    else:
        system('cls')
        print(f'{expresion} NO está balanceada =(')
