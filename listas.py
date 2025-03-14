from os import system
import Pilas

def verificaAgrupador(expresion):
    P = Pilas.Pila()

    parejas = { '(':')', '[':']', '{':'}', '<':'>' }

    for agrupador in expresion:
        if agrupador in parejas:
            P.push( parejas.get(agrupador) )

        elif agrupador in parejas.values() and P.estaVacia():
            return False
        
        elif agrupador in parejas.values() and not P.estaVacia() and P.pop()!=agrupador:
            return False

    if P.estaVacia():
        return True
    else:
        return False

if __name__ == '__main__':
    system('cls')
    
    expresion = input('Ingresa expresión ')
    
    if verificaAgrupador(expresion):
        print(f'{expresion} ESTÁ balanceada =)')
    else:
        system('cls')
        print(f'{expresion} NO está balanceada =(')
