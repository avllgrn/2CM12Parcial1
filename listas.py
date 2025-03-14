from os import system
import Pilas

def verificaParentesis(expresion):
    P = Pilas.Pila()

    for parentesis in expresion:
        if parentesis is '(':
            P.push(')')
        elif parentesis is ')' and P.estaVacia():
            return False
        elif parentesis is ')' and not P.estaVacia():
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
