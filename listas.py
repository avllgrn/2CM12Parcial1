from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    A = set()    #Conjunto vacio ***Cuidado*** NO es {}
    print(f'conjunto={A} type={type(A)}', end=' ')
    print(f'len={len(A)}',end='\n\n')

    while len(A)<10:
        x = randrange(101)
        print(f'Se intenta agregar {x} en A')
        A.add(x)
        print(f'conjunto={A} type={type(A)}', end=' ')
        print(f'len={len(A)}',end='\n\n')
        
    B = set()    #Conjunto vacio ***Cuidado*** NO es {}
    print(f'conjunto={B} type={type(B)}', end=' ')
    print(f'len={len(B)}',end='\n\n')

    while len(B)<10:
        x = randrange(101)
        print(f'Se intenta agregar {x} en B')
        B.add(x)
        print(f'conjunto={B} type={type(B)}', end=' ')
        print(f'len={len(B)}',end='\n\n')
        

    print(f'A={A}')
    for dato in A:
        print(dato)
    print()
    
    print(f'B={B}')
    for dato in B:
        print(dato)
    print()
    
    U = A.union(B)
    print(f'A U B={U}')
    for dato in U:
        print(dato)
    print()
    
    I = A.intersection(B)
    print(f'A ∩ B={I}')
    for dato in I:
        print(dato)
    print()
