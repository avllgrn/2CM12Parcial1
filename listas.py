from os import system

if __name__ == '__main__':
    system('cls')

    conjunto = set()    #Conjunto vacio ***Cuidado*** NO es {}
    print(f'conjunto={conjunto} type={type(conjunto)}', end=' ')
    print(f'len={len(conjunto)}',end='\n\n')

    conjunto = {1, 3, 5, 7, 9}  # Conjunto inicializado
    print(f'conjunto={conjunto} type={type(conjunto)}', end=' ')
    print(f'len={len(conjunto)}',end='\n\n')

    conjunto.add(11)    #Se agrega un elemento a un conjunto
    print(f'conjunto={conjunto} type={type(conjunto)}', end=' ')
    print(f'len={len(conjunto)}',end='\n\n')

    conjunto.add(3) #No pueden agregarse elementos ya existentes
    print(f'conjunto={conjunto} type={type(conjunto)}', end=' ')
    print(f'len={len(conjunto)}',end='\n\n')
   
    conjunto.add(7)
    print(f'conjunto={conjunto} type={type(conjunto)}', end=' ')
    print(f'len={len(conjunto)}',end='\n\n')    
