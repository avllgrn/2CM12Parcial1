from os import system
from random import randrange

def creaPares(n):

    pares = set()
    while len(pares) < n:
        x = randrange(101)
        # print(f'Intenta ingresarse {x} ')
        if x%2 == 0:
            pares.add(x)
        #print(pares, type(pares), len(pares))    
    #print(pares, type(pares), len(pares))

    for numero in pares:
        print(numero)

def creaImpares(n):

    impares = set()
    while len(impares) < n:
        x = randrange(101)
        #print(f'Intenta ingresarse {x} ')
        if x%2 != 0:
            impares.add(x)
        #print(impares, type(impares), len(impares))

    #print(impares, type(impares), len(impares))

    for numero in impares:
        print(numero)

def esPrimo(x):

    if x < 2:
        return False

    for i in range(2, x):
        if x%i == 0:
            return False        
    return True

def creaPrimos(n):
    primos = set()

    while len(primos) < n:
        x = randrange(101)
        # print(f'Intenta ingresarse {x} ')
        if esPrimo(x):
            primos.add(x)
        # print(primos, type(primos), len(primos))
    # print(primos, type(primos), len(primos))

    for numero in primos:
        print(numero)

def menu():
    print('1. Pares')
    print('2. Impares')
    print('3. Primos')
    print('4. Salir')
    return input('Cuál es tu opción? ')    

def casos(opcion):
    match opcion:
        case '1':
            creaPares(int(input('Cuántos? ')))
            system('pause')
        case '2':
            creaImpares(int(input('Cuántos? ')))
            system('pause')
        case '3':
            creaPrimos(int(input('Cuántos? ')))
            system('pause')
        case '4':
            print('Adiós!')
        case _:
            print('Opción inválida!')
            system('pause')

if __name__ == '__main__':
    system('cls')
    
    opcion = None
    while opcion!='4':
        system('cls')
        opcion = menu()
        casos(opcion)
