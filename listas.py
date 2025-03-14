from os import system
import Pilas

def verificaParentesis(expresion):
    P = Pilas.Pila()

    for parentesis in expresion:
        if parentesis == '(':
            P.push( ')' )

        elif parentesis == '[':
            P.push( ']' )

        elif parentesis == '{':
            P.push( '}' )

        elif parentesis == '<':
            P.push( '>' )

        elif (parentesis == ')' or parentesis == ']' or 
              parentesis == '}' or parentesis == '>') and P.estaVacia():
            return False
        
        elif (parentesis == ')' or parentesis == ']' or 
              parentesis == '}' or parentesis == '>') and not P.estaVacia():
            if P.pop()!=parentesis:
                return False

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
